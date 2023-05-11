import os

# Copied from distutils.util.strtobool, which is deprecated
def strtobool (val):
    """Convert a string representation of truth to true (1) or false (0).

    True values are case insensitive 'y', 'yes', 't', 'true', 'on', and '1'.
    false values are case insensitive 'n', 'no', 'f', 'false', 'off', and '0'.
    Raises ValueError if 'val' is anything else.
    """
    val = val.lower()
    if val in ('y', 'yes', 't', 'true', 'on', '1'):
        return 1
    elif val in ('n', 'no', 'f', 'false', 'off', '0'):
        return 0
    else:
        raise ValueError("invalid truth value %r" % (val,))

INVERTER_SERIAL = int(os.environ.get('INVERTER_SERIAL'))
INVERTER_ADDRESS = os.environ.get('INVERTER_ADDRESS')
INVERTER_PORT = int(os.environ.get('INVERTER_PORT', 8899))

MQTT_ENABLED = strtobool(os.environ.get('MQTT_ENABLED', 'True'))
if MQTT_ENABLED:
    MQTT_SERVER = os.environ.get('MQTT_SERVER')
    MQTT_PORT = int(os.environ.get('MQTT_PORT', 1883))
    MQTT_TOPIC = os.environ.get('MQTT_TOPIC', "solis/METRICS")
    MQTT_USER = os.environ.get('MQTT_USER', "solarman-exporter")
    MQTT_PASS = os.environ.get('MQTT_PASS')
    MQTT_KEEPALIVE = int(os.environ.get('MQTT_KEEPALIVE', 60))

# How often to check(seconds), only applies when 'PROMETHEUS = False' otherwise uses Prometheus scrape interval
CHECK_INTERVAL = int(os.environ.get('CHECK_INTERVAL', 30))
PROMETHEUS_ENABLED = strtobool(os.environ.get('PROMETHEUS', 'True'))
PROMETHEUS_PREFIX = os.environ.get('PROMETHEUS_PREFIX', 'solarman_')
PROMETHEUS_PORT = int(os.environ.get('PROMETHEUS_PORT', 18000))

LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
