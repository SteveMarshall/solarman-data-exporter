import os

INVERTER_SERIAL = os.environ.get('INVERTER_SERIAL')
INVERTER_ADDRESS = os.environ.get('INVERTER_ADDRESS')
INVERTER_PORT = os.environ.get('INVERTER_PORT', 8899)

MQTT_ENABLED = os.environ.get('MQTT_ENABLED', True)
if MQTT_ENABLED:
    MQTT_SERVER = os.environ.get('MQTT_SERVER')
    MQTT_PORT = os.environ.get('MQTT_PORT', 1883)
    MQTT_TOPIC = os.environ.get('MQTT_TOPIC', "solis/METRICS")
    MQTT_USER = os.environ.get('MQTT_USER', "solarman-exporter")
    MQTT_PASS = os.environ.get('MQTT_PASS')
    MQTT_KEEPALIVE = os.environ.get('MQTT_KEEPALIVE', 60)

# How often to check(seconds), only applies when 'PROMETHEUS = False' otherwise uses Prometheus scrape interval
CHECK_INTERVAL = os.environ.get('CHECK_INTERVAL', 30)
PROMETHEUS_ENABLED = os.environ.get('PROMETHEUS', True)
PROMETHEUS_PORT = os.environ.get('PROMETHEUS_PORT', 18000)

LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
