# MODBUS Registers, prometheus name and description
# Add * in front of the register name if you do not want it to be presented to Prometheus or published to MQTT
from registers import (
    RegisterSet as RS,
    Register as R,
    FormattedRegisterSet as FRS
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
        R('grid_voltage_a', 'Grid A voltage (0.1V)'),
        R('grid_current_a', 'Grid A current (0.01A)'),
        R('grid_voltage_b', 'Grid B voltage (0.1V)'),
        R('grid_current_b', 'Grid B current (0.01A)'),
        R('grid_voltage_c', 'Grid C voltage (0.1V)'),
        R('grid_current_c', 'Grid C current (0.01A)'),
        R('grid_frequency', 'Grid frequency (0.01Hz)'),
        R('battery_charge_power', 'Battery charge/discharge power (0.01KW)'),
        R('battery_voltage', 'Battery voltage (0.1V)'),
        R('battery_current', 'Battery charge/discharge current (0.01A)'),
        R('battery_capacity_soc', 'Battery charge (%)'),
        R('battery_temperature', 'Battery temperature (0.1C)'),
        R('feed_in_power', 'Feed in power (0.01KW)'),
        R('consumption_power', 'Consumtion power (0.01KW)'),
        R('inout_power', 'Input/Output power (0.01KW)'),
        R('generation_power', 'Generation power (0.01KW)'),
        R('eps_voltage', 'EPS Voltage (0.1V)'),
        R('eps_power', 'EPS Power (0.01KW)'),
    )),

    RS(0x218, (
        R('today_generated_power', 'Today\'s generated power (0.01KWh)'),
        R('today_exported_power', 'Today\'s exported power (0.01KWh)'),
        R('today_imported_power', 'Today\'s imported power (0.01KWh)'),
        R('today_consumption_power', 'Today\'s power consumption (0.01KWh)'),
    )),

    FRS(0x21C, register_size=2, registers=(
        R('total_generated_power', 'Total generated power (1KWh)'),
        R('total_exported_power', 'Total exported power (1KWh)'),
        R('total_imported_power', 'Total imported power (1KWh)'),
        R('total_consumption', 'Total power consumption (1KWh)'),
    )),

    RS(0x243, (
        R('today_generation_time', 'Today\'s generation time (1 min)'),
    )),
    FRS(0x244, register_size=2, registers=(
        R('total_generation_time', 'Total generation time (hours)'),
    )),

    RS(0x22A, (
        R('countdown_time', 'Countdown time'),
        R('inverter_alert', 'Inverter alert code'),
        R('battery_cycles', 'Battery cycles'),
        R('inv_bus_voltage', 'INV bus voltage'),
        R('llc_bus_voltage', 'LLC bus voltage'),
        R('buck_current', 'Buck current'),
        R('grid_voltage_r', 'Grid R voltage (0.1V)'),
        R('grid_current_r', 'Grid R current (0.01A)'),
        R('grid_voltage_s', 'Grid S voltage (0.1V)'),
        R('grid_current_s', 'Grid S current (0.01A)'),
        R('grid_voltage_t', 'Grid T voltage (0.1V)'),
        R('grid_current_t', 'Grid T current (0.01A)'),
        R('generation_current', 'Generation current (?)'),
        R('battery_power', 'Battery power (?)'),
        R('inverter_temperature', 'Inverter temperature (1C)'),
        R('heat_sink_temperature', 'Heat sink temperature (1C)'),
        R('country', 'Country'),
        R('current_dc_component', 'Current DC component(1mA)'),
        R('voltage_dc_component', 'Voltage DC component (0.1V)'),
    )),
)
