# ver. 0.0.29
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

metrics_dict = {}

def scrape_solis():
    custom_metrics_dict = {}
    global metrics_dict
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

    logging.info('Scraping...')

    for r in registers.all_regs:
        reg = r[0]
        reg_len = len(r[1])
        reg_des = r[1]

        # Sometimes the query fails this will retry 3 times before exiting
        c = 0
        while True:
            try:
                logging.debug(f'Scrapping registers {reg} length {reg_len}')
                # read registers at address , store result in regs list
                regs = modbus.read_holding_registers(register_addr=reg, quantity=reg_len)
                logging.debug(regs)
            except Exception as e:
                if c == 3:
                    logging.error(f'Cannot read registers {reg} length{reg_len}. Tried {c} times. Exiting {repr(e)}')
                    exit(1)
                else:
                    c += 1
                    logging.error(f'Cannot read registers {reg} length {reg_len} {repr(e)}')
                    logging.error(f'Retry {c} in 3s')
                    sleep(3)  # hold before retry
                    continue
            break

        # Add metric to list

        for (i, item) in enumerate(regs):
            if '*' not in reg_des[i][0]:
                metrics_dict[reg_des[i][0]] = reg_des[i][1], item
            else:
                regs_ignored += 1

    logging.info(f'Ignored registers: {regs_ignored}')

    logging.info('Scraped')


def publish_mqtt():
    mqtt_dict = {}
    try:
        if not config.PROMETHEUS_ENABLED:
            scrape_solis()

        # Resize dictionary and convert to JSON
        for metric, value in metrics_dict.items():
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
        scrape_solis()

        for metric, value in metrics_dict.items():
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
