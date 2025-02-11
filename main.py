import config.config as config
import config.registers as register_config
import logging
import paho.mqtt.client as mqtt
from itertools import chain
from sys import exit
from json import dumps
from time import strptime, mktime, sleep
from threading import Lock
from prometheus_client import start_http_server
from prometheus_client.core import GaugeMetricFamily, REGISTRY
from pysolarmanv5 import PySolarmanV5

def retry(function, times=3, delay=3):
    # We want one initial attempt and `times` retries
    tries = times + 1
    for retry in range(tries):
        try:
            return function()
        except Exception as e:
            if retry == tries:
                logging.exception(
                    f'Retry limit of {times} reached for {function}. Exiting.'
                )
                exit(1)
            logging.exception(
                f'{function} failed. Retry #{retry} in {delay}s'
            )
            sleep(delay)


def get_metrics_reader(
    inverter_address,
    inverter_serial,
    inverter_port,
    modbus_lock
):
    if modbus_lock.locked():
        logging.info('Mobdus connection in use; waiting…')
    modbus_lock.acquire()

    logging.info('Connecting to data logger…')
    try:
        modbus = retry(lambda: PySolarmanV5(
            inverter_address,
            inverter_serial,
            port=inverter_port
        ))
    except Exception as e:
        modbus_lock.release()
        raise e

    logging.info('Building lazy-loading metrics readers…')

    metric_sets = map(
        lambda register_set: retry(
            lambda: register_set.read_metrics(modbus)
        ),
        register_config.all
    )
    logging.info('Yielding metrics')
    try:
        yield from chain.from_iterable(metric_sets)
    except Exception as e:
        modbus_lock.release()
        raise e

    logging.info('Finished yielding metrics; closing modbus')

    modbus.disconnect()
    modbus_lock.release()


def publish_mqtt(get_metrics_reader):
    mqtt_dict = {}
    try:
        metrics_reader = get_metrics_reader()

        # Convert metrics to JSON
        for metric in metrics_reader:
            mqtt_dict[metric.label] = metric.value
        mqtt_json = dumps(mqtt_dict)

        def on_message(mqttc, userdata, msg):
            print(f"Message received [{msg.topic}]: {msg.payload}")


        mqttc = mqtt.Client()
        if config.MQTT_USER != '':
            mqttc.username_pw_set(config.MQTT_USER, config.MQTT_PASS)
        mqttc.connect(config.MQTT_SERVER, config.MQTT_PORT, config.MQTT_KEEPALIVE)
        mqttc.on_connect = logging.info(f'Connected to MQTT {config.MQTT_SERVER}:{config.MQTT_PORT}')

        logging.info('Publishing MQTT')
        mqttc.publish(topic=config.MQTT_TOPIC, payload=mqtt_json)

        mqttc.disconnect()

    except Exception as e:
        logging.error(f'Could not connect to MQTT {repr(e)}')


class CustomCollector(object):
    def __init__(self, get_metrics_reader):
        self.get_metrics_reader = get_metrics_reader

    def collect(self):
        logging.info('Prometheus collection started')
        metrics_reader = self.get_metrics_reader()

        for metric in metrics_reader:
            logging.debug(f'Generating gauge {config.PROMETHEUS_PREFIX}{metric.label}')
            yield GaugeMetricFamily(
                f'{config.PROMETHEUS_PREFIX}{metric.label}',
                metric.description,
                metric.value
            )

        logging.info('Prometheus collection ended')


if __name__ == '__main__':
    try:
        if not (config.MQTT_ENABLED or config.PROMETHEUS_ENABLED):
            logging.error(f'Cannot start: no exporters enabled')
            exit(1)

        logging.basicConfig(
            format='%(asctime)s %(levelname)s:%(name)s %(message)s',
            level=config.LOGLEVEL,
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        modbus_lock = Lock()

        if config.PROMETHEUS_ENABLED:
            logging.info(f'Starting Web Server for Prometheus on port: {config.PROMETHEUS_PORT}')
            start_http_server(config.PROMETHEUS_PORT)

            REGISTRY.register(CustomCollector(
                lambda: get_metrics_reader(
                    config.INVERTER_ADDRESS,
                    config.INVERTER_SERIAL,
                    config.INVERTER_PORT,
                    modbus_lock
                )
            ))

        while True:
            if config.MQTT_ENABLED:
                publish_mqtt(lambda: get_metrics_reader(
                    config.INVERTER_ADDRESS,
                    config.INVERTER_SERIAL,
                    config.INVERTER_PORT,
                    modbus_lock
                ))
            sleep(config.CHECK_INTERVAL)

    except:
        logging.exception(f'Cannot start')
        exit(1)
