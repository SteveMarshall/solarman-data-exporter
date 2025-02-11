# MODBUS Registers, prometheus name and description
# Add * in front of the register name if you do not want it to be presented to Prometheus or published to MQTT
from registers import (
    RegisterSet as RS,
    Register as R,
)

all = (
    RS(0x200, (
        R('running_state', 'Running state'),
        R('fault_code_1', 'Fault code 1'),
        R('fault_code_2', 'Fault code 2'),
        R('fault_code_3', 'Fault code 3'),
        R('fault_code_4', 'Fault code 4'),
        R('fault_code_5', 'Fault code 5'),
    )),

    RS(0x23D, (
        R('battery_fault_code_1', 'Battery fault code 1'),
        R('battery_fault_code_2', 'Battery fault code 2'),
        R('battery_fault_code_3', 'Battery fault code 3'),
        R('battery_fault_code_4', 'Battery fault code 4'),
        R('battery_fault_code_5', 'Battery fault code 5'),
    )),

    RS(0x206, (
        R('grid_voltage_a', 'Grid A voltage (V)', scale=0.1),
        R('grid_current_a', 'Grid A current (A)', scale=0.01, signed=True),
        R('grid_voltage_b', 'Grid B voltage (V)', scale=0.1),
        R('grid_current_b', 'Grid B current (A)', scale=0.01, signed=True),
        R('grid_voltage_c', 'Grid C voltage (V)', scale=0.1),
        R('grid_current_c', 'Grid C current (A)', scale=0.01, signed=True),
        R('grid_frequency', 'Grid frequency (Hz)', scale=0.01),
        R('battery_charge_power', 'Battery charge power (W)', scale=10, signed=True),
        R('battery_voltage', 'Battery voltage (V)', scale=0.1),
        R('battery_charge_current', 'Battery charge current (A)', scale=0.01, signed=True),
        R('battery_capacity_soc', 'Battery charge (%)'),
        R('battery_temperature', 'Battery temperature (°C)'),
        R('feed_in_power', 'Feed in power (W)', scale=10, signed=True),
        R('consumption_power', 'Consumtion power (W)', scale=10),
        R('inout_power', 'Input/Output power (W)', scale=10, signed=True),
        R('generation_power', 'Generation power (W)', scale=10),
        R('eps_voltage', 'EPS Voltage (V)', scale=0.1),
        R('eps_power', 'EPS Power (W)', scale=10),
    )),

    RS(0x218, (
        R('today_generated_power', 'Today\'s generated power (Wh)', scale=10),
        R('today_exported_power', 'Today\'s exported power (Wh)', scale=10),
        R('today_imported_power', 'Today\'s imported power (Wh)', scale=10),
        R('today_consumption_power', 'Today\'s power consumption (Wh)', scale=10),
    )),

    RS(0x21C, (
        R('total_generated_power', 'Total generated power (KWh)', size=2),
        R('total_exported_power', 'Total exported power (KWh)', size=2),
        R('total_imported_power', 'Total imported power (KWh)', size=2),
        R('total_consumption', 'Total power consumption (KWh)', size=2),
    )),

    RS(0x243, (
        R('today_generation_time', 'Today\'s generation time (minutes)'),
        R('total_generation_time', 'Total generation time (hours)', size=2),
    )),

    RS(0x22A, (
        R('countdown_time', 'Countdown time'),
        R('inverter_alert', 'Inverter alert code'),
        R('battery_cycles', 'Battery cycles'),
        R('inv_bus_voltage', 'INV bus voltage'),
        R('llc_bus_voltage', 'LLC bus voltage'),
        R('buck_current', 'Buck current'),
        R('grid_voltage_r', 'Grid R voltage (V)', scale=0.1),
        R('grid_current_r', 'Grid R current (A)', scale=0.01, signed=True),
        R('grid_voltage_s', 'Grid S voltage (V)', scale=0.1),
        R('grid_current_s', 'Grid S current (A)', scale=0.01, signed=True),
        R('grid_voltage_t', 'Grid T voltage (V)', scale=0.1),
        R('grid_current_t', 'Grid T current (A)', scale=0.01, signed=True),
        R('generation_current', 'Generation current (?)', signed=True),
        R('battery_power', 'Battery power (?)'),
        R('inverter_temperature', 'Inverter temperature (°C)', signed=True),
        R('heat_sink_temperature', 'Heat sink temperature (°C)', signed=True),
        R('country', 'Country'),
        R('current_dc_component', 'Current DC component(mA)', signed=True),
        R('voltage_dc_component', 'Voltage DC component (V)', scale=0.1),
    )),
)
