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
        logging.info('Connecting to Solis Modbus')
        modbus = PySolarmanV5(
            config.INVERTER_IP,
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
                regs = modbus.read_input_registers(register_addr=reg, quantity=reg_len)
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

        # Convert time to epoch
        if reg == 33022:
            inv_year = '20' + str(regs[0]) + '-'
            if regs[1] < 10:
                inv_month = '0' + str(regs[1]) + '-'
            else:
                inv_month = str(regs[1]) + '-'
            if regs[2] < 10:
                inv_day = '0' + str(regs[2]) + ' '
            else:
                inv_day = str(regs[2]) + ' '
            if regs[3] < 10:
                inv_hour = '0' + str(regs[3]) + ':'
            else:
                inv_hour = str(regs[3]) + ':'
            if regs[4] < 10:
                inv_min = '0' + str(regs[4]) + ':'
            else:
                inv_min = str(regs[4]) + ':'
            if regs[5] < 10:
                inv_sec = '0' + str(regs[5])
            else:
                inv_sec = str(regs[5])
            inv_time = inv_year + inv_month + inv_day + inv_hour + inv_min + inv_sec
            logging.info(f'Solis Inverter time: {inv_time}')
            time_tuple = strptime(inv_time, '%Y-%m-%d %H:%M:%S')
            time_epoch = mktime(time_tuple)
            metrics_dict['system_epoch'] = 'System Epoch Time', time_epoch

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
        if not config.PROMETHEUS:
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
            yield GaugeMetricFamily(metric, value[0], value=value[1])


if __name__ == '__main__':
    try:
        if not (config.MQTT or config.PROMETHEUS):
            logging.error(f'Cannot start: no exporters enabled')
            exit(1)

        logging.basicConfig(
            format='%(asctime)s %(levelname)s:%(name)s %(message)s',
            level=config.LOGLEVEL,
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        logging.info('Starting')

        if config.PROMETHEUS:
            logging.info(f'Starting Web Server for Prometheus on port: {config.PROMETHEUS_PORT}')
            start_http_server(config.PROMETHEUS_PORT)

            REGISTRY.register(CustomCollector())

        while True:
            if config.MQTT:
                publish_mqtt()
            sleep(config.CHECK_INTERVAL)

    except Exception as e:
        logging.error(f'Cannot start: {repr(e)}')
        exit(1)
