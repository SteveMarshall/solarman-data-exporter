import config.config as config
import config.registers as registers
import logging
import paho.mqtt.client as mqtt
from sys import exit
from json import dumps
from time import strptime, mktime, sleep
from prometheus_client import start_http_server
from prometheus_client.core import GaugeMetricFamily, REGISTRY
from pysolarmanv5.pysolarmanv5 import PySolarmanV5

def query_datalogger():
    metrics_dict = {}
    regs_ignored = 0
    try:
        logging.info('Connecting to Solarman ModBus interface')
        modbus = PySolarmanV5(
            config.INVERTER_ADDRESS,
            config.INVERTER_SERIAL,
            port=config.INVERTER_PORT
        )
    except Exception as e:
        logging.error(f'{repr(e)}. Exiting')
        exit(1)

    logging.info('Connected')

    for r in registers.all_regs:
        address = r[0]
        quantity = len(r[1])
        reg_descriptions = r[1]

        # Sometimes the query fails this will retry 3 times before exiting
        for retry in range(0, 3):
            try:
                logging.debug(f'Reading registers at {address}, quantity {quantity}')

                regs = modbus.read_holding_registers(
                    register_addr=address,
                    quantity=reg_len
                )
                logging.debug(regs)
            except Exception as e:
                if retry == 3:
                    logging.error(f'Cannot read registers at {address}, quantity {quantity}. Tried {retry} times. Exiting {repr(e)}')
                    exit(1)
                logging.error(f'Cannot read registers {address}, quantity {quantity} {repr(e)}')
                logging.error(f'Retry {retry} in 3s')
                sleep(3)
                continue
            break

        # Add metric to list
        for (i, item) in enumerate(regs):
            if '*' not in reg_descriptions[i][0]:
                metrics_dict[reg_descriptions[i][0]] = reg_descriptions[i][1], item
            else:
                regs_ignored += 1

    logging.info(f'Ignored registers: {regs_ignored}')

    logging.info('Finished')

    return metrics_dict


def publish_mqtt():
    mqtt_dict = {}
    try:
        metrics = query_datalogger()

        # Resize dictionary and convert to JSON
        for metric, value in metrics.items():
            mqtt_dict[metric] = value[1]
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
    def __init__(self):
        pass

    def collect(self):
        metrics = query_datalogger()

        for metric, value in metrics.items():
            yield GaugeMetricFamily(
                f'{config.PROMETHEUS_PREFIX}{metric}',
                value[0],
                value=value[1]
            )


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

        logging.info('Starting')

        if config.PROMETHEUS_ENABLED:
            logging.info(f'Starting Web Server for Prometheus on port: {config.PROMETHEUS_PORT}')
            start_http_server(config.PROMETHEUS_PORT)

            REGISTRY.register(CustomCollector())

        while True:
            if config.MQTT_ENABLED:
                publish_mqtt()
            sleep(config.CHECK_INTERVAL)

    except Exception as e:
        logging.error(f'Cannot start: {repr(e)}')
        exit(1)
