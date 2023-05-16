# Solarman Data Exporter

This is a collection of utilities to collect data from Solarman wifi
data logging sticks and publish them to one or both of Prometheus and
MQTT.

This is based on the work of
[NosIreland](https://github.com/NosIreland/solismon3) and
[jmccrohan](https://github.com/jmccrohan/pysolarmanv5).

The data is pulled directly from the Solarman WiFi stick. You need to
provide the address and serial number of the stick.

The registers to be read are described in `config/registers.py`. I have
defined registers that (appear to) work for my Sofar Solar HYD-3600 ES,
but **your inverter will likely need a different configuration**.

## Configuration

### Environment variables

This script can be configured using the following environment variables:

- `INVERTER_ADDRESS` (no default): IP address or hostname of data
  logging stick
- `INVERTER_SERIAL` (no default): Serial number of the data logging
  stick (not inverter!)
- `INVERTER_PORT` (default: `8899`): TCP port to connect to data
  logging stick
- `MQTT_ENABLED` (default: `True`): Whether to publish metrics to MQTT
- `MQTT_SERVER` (no default): IP address or hostname of MQTT server
- `MQTT_PORT` (default: `1883`): TCP port to connect to MQTT server
- `MQTT_USER` (default: `solarman-exporter`): Username for MQTT server
- `MQTT_PASS` (no default): Password for MQTT server
- `MQTT_TOPIC` (default: `solis/METRICS`): Topic on which to publish
  MQTT messages
- `MQTT_KEEPALIVE` (default: `60`): MQTT keepalive
- `CHECK_INTERVAL` (default: `30`): How often to scrape metrics in
  seconds, only applies when 'PROMETHEUS = False' otherwise uses
  Prometheus scrape interval
- `PROMETHEUS_ENABLED` (default: `True`): Whether to publish metrics
  for Prometheus
- `PROMETHEUS_PREFIX` (default: `solarman_`): Prefix to apply to all
  metrics exported to Prometheus
- `PROMETHEUS_PORT` (default: `18000`): TCP port to expose Prometheus
  metrics on
- `LOGLEVEL` (default: `INFO`): Set the level of detail at which to
  output log messages.

### Inverter-specific configuration

Many inverters export metrics as “registers” using the [Modbus
protocol](https://en.wikipedia.org/wiki/Modbus), but these **registers
aren't the same on all inverters**, and aren't necessarily even the
same type of registers: my inverter primarily uses "holding" registers,
where others use mostly "input" registers.

I have defined registers that (appear to) work for my Sofar Solar
HYD-3600 ES in [`config/registers.py`](./config/registers.py). The
configuration is based on the [Sofar Solar ModBus protocol
manual](./examples/SOFARSOLAR-ModBus-RTU-Communication-Protocol.pdf)
(that I found online and seemed to work).

To configure this project for your inverter, you need to create a
`config/registers.py` file of your own (unless mine happens to work for
you, too).

#### Writing your inverter configuration

Registers are defined in sets to try to make it easy to read them in
groups, which is (probably?) faster than reading them one at a time.

There are (at the moment) three types of building blocks for the
inverter configuration:

- `RegisterSet`: Groups of registers. They have an address
  (either an integer or hex address code is fine) and a list of
  `Register`s.
- `Register`: The label and description for a given metric; the former
  will be the basis of the Prometheus or MQTT IDs for the metric. They
  can also optionally have a `size` (for multi-byte registers) or be
  `signed` (i.e. have a value that can be negative or positive).

To work out what registers your inverter uses, you'll need to look for
the Modbus protocol documentation for your inverter or one from the
same range/manufacturer. You can also try running
[`examples/register_scan.py`](./examples/register_scan.py), but that
was only useful for me once I knew the type of registers my inverter
used, and roughly what addresses to look at.

Your `config/registers.py` should look something like this (albeit much
longer):

```python
# Use shorthands for Register and RegisterSet
from registers import (
    Register as R,
    RegisterSet as RS,
)

all = (
    # Four registers at addresses 0x200, 0x201, 0x203, etc
    RS(0x200, (
        R('running_state', 'Running state'),
        R('fault_code_1', 'Fault code 1'),
        R('fault_code_2', 'Fault code 2'),
        R('fault_code_3', 'Fault code 3'),
        R('fault_code_4', 'Fault code 4'),
    )),

    # One register that can be negative or positive, at address 0x207
    RS(0x207, (
        R('grid_current_a', 'Grid A current (0.01A)', signed=True),
    )),

    # Four 2-register-long registers, at addresses 0x21C, 0x21E, etc
    RS(0x21C, (
        R('total_generated_power', 'Total generated power (1KWh)', size=2),
        R('total_exported_power', 'Total exported power (1KWh)', size=2),
        R('total_imported_power', 'Total imported power (1KWh)', size=2),
        R('total_consumption', 'Total power consumption (1KWh)', size=2),
    )),
)
```

## Running

### Running in Docker

This repo is available as a [pre-built Docker
container](https://hub.docker.com/r/stevemarshall/solarman-data-exporter).

To use it, run:

```
docker run -it -d \
  --restart unless-stopped \
  -e "INVERTER_ADDRESS=${INVERTER_ADDRESS}"
  -e "INVERTER_SERIAL=${INVERTER_SERIAL}"
  -e "MQTT_ENABLED=False"
  -p 18000:18000
  stevemarshall/solarman-data-exporter
```

### Running in Docker Compose

Add something along these lines to your `docker-compose.yml`:

```
services:
  solarman-data-exporter:
    image: stevemarshall/solarman-data-exporter
    environment:
      - INVERTER_ADDRESS=${INVERTER_ADDRESS}
      - INVERTER_SERIAL=${INVERTER_SERIAL}
      - MQTT_ENABLED=False
    ports:
      - 18000:18000
    restart: always
```

Then run `docker compose up`, and open [the
metrics](http://localhost:18000/).
