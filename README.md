# Solarman Data Exporter

This is a collection of utilities to collect data from Solarman wifi
data logging sticks and publish them to one or both of Prometheus and
MQTT.

This is based on the work of
[NosIreland](https://github.com/NosIreland/solismon3) and
[jmccrohan](https://github.com/jmccrohan/pysolarmanv5).

The data is pulled directly from the Solarman WiFi stick. You need to
provide the address and serial number of the stick.

The registers to be polled and their meaning are stored in `registers.py` file. I have populated file already with registers that I use. The list is not final but shoudl be good enough for most cases. Note the registers are not the same on all models and firmware versions. They do tend to move with firmware upgrades. You may need to adjusts or add new ones for the inverter that you use.

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

### registers.py
I have registers predefined for single phase Solis RHI 4G hybrid inverter in [registers.py](./config/registers.py) file. 
The register mappings are not the same on all inverters. Non-hybrid inverters have different mapping, so you will need to adjust. 
I will try to add more later on.   
The registers are read in blocks as that is much faster than reading individual registers one by one.    
In registers.py you need to provide:   
Register number you want to start with(integer), register name(string, no space allowed, use '_'), register description(string)   
Add '*' in front of register name if you want it to be skipped. 

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

### Testing
To see if it is running properly I would advise enabling debugging `DEBUG = False` and also `PROMETHEUS = True`
(you do not need to have Prometheus installed) for testing. Once started check container logs `docker logs solismon3` and in 
browser enter url http://docker_host_ip:18000. Assuming all is ok, you should see metrics in browser. 

If program fails with default [registers.py](./config/registers.py) you can try scanning registers with 
[register_scan](./examples/register_scan.py) and see if you can get anything. For non-hybrid inverter start with 1000 and go up.

## Important
This is a very early draft version and things might not work as expected. Feel free to ask questions.
