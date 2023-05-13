# MODBUS Registers, prometheus name and description
# Add * in front of the register name if you do not want it to be presented to Prometheus or published to MQTT

all_regs = (
    (0x200, (
        ('running_state', 'Running state'),
        ('fault_code_1', 'Fault code 1'),
        ('fault_code_2', 'Fault code 2'),
        ('fault_code_3', 'Fault code 3'),
        ('fault_code_4', 'Fault code 4'),
        ('fault_code_5', 'Fault code 5'),
    )),

    (0x23D, (
        ('battery_fault_code_1', 'Battery fault code 1'),
        ('battery_fault_code_2', 'Battery fault code 2'),
        ('battery_fault_code_3', 'Battery fault code 3'),
        ('battery_fault_code_4', 'Battery fault code 4'),
        ('battery_fault_code_5', 'Battery fault code 5'),
    )),

    (0x206, (
        ('grid_voltage_a', 'Grid A voltage (0.1V)'),
        ('grid_current_a', 'Grid A current (0.01A)'),
        ('grid_voltage_b', 'Grid B voltage (0.1V)'),
        ('grid_current_b', 'Grid B current (0.01A)'),
        ('grid_voltage_c', 'Grid C voltage (0.1V)'),
        ('grid_current_c', 'Grid C current (0.01A)'),
        ('grid_frequency', 'Grid frequency (0.01Hz)'),
        ('battery_charge_power', 'Battery charge/discharge power (0.01KW)'),
        ('battery_voltage', 'Battery voltage (0.1V)'),
        ('battery_current', 'Battery charge/discharge current (0.01A)'),
        ('battery_capacity_soc', 'Battery charge (%)'),
        ('battery_temperature', 'Battery temperature (0.1C)'),
        ('feed_in_power', 'Feed in power (0.01KW)'),
        ('consumption_power', 'Consumtion power (0.01KW)'),
        ('inout_power', 'Input/Output power (0.01KW)'),
        ('generation_power', 'Generation power (0.01KW)'),
        ('eps_voltage', 'EPS Voltage (0.1V)'),
        ('eps_power', 'EPS Power (0.01KW)'),
    )),

    (0x218, (
        ('today_generated_power', 'Today\'s generated power (0.01KWh)'),
        ('today_exported_power', 'Today\'s exported power (0.01KWh)'),
        ('today_imported_power', 'Today\'s imported power (0.01KWh)'),
        ('today_consumption_power', 'Today\'s power consumption (0.01KWh)'),
    )),

    (0x21C, (
        ('total_generated_power', 'Total generated power (1KWh)'),
        ('total_exported_power', 'Total exported power (1KWh)'),
        ('total_imported_power', 'Total imported power (1KWh)'),
        ('total_consumption', 'Total power consumption (1KWh)'),
    ), 2),

    (0x243, (
        ('today_generation_time', 'Today\'s generation time (1 min)'),
    )),
    (0x244, (
        ('total_generation_time', 'Total generation time (hours)'),
    ), 2),

    (0x22A, (
        ('countdown_time', 'Countdown time'),
        ('inverter_alert', 'Inverter alert code'),
        ('battery_cycles', 'Battery cycles'),
        ('inv_bus_voltage', 'INV bus voltage'),
        ('llc_bus_voltage', 'LLC bus voltage'),
        ('buck_current', 'Buck current'),
        ('grid_voltage_r', 'Grid R voltage (0.1V)'),
        ('grid_current_r', 'Grid R current (0.01A)'),
        ('grid_voltage_s', 'Grid S voltage (0.1V)'),
        ('grid_current_s', 'Grid S current (0.01A)'),
        ('grid_voltage_t', 'Grid T voltage (0.1V)'),
        ('grid_current_t', 'Grid T current (0.01A)'),
        ('generation_current', 'Generation current (?)'),
        ('battery_power', 'Battery power (?)'),
        ('inverter_temperature', 'Inverter temperature (1C)'),
        ('heat_sink_temperature', 'Heat sink temperature (1C)'),
        ('country', 'Country'),
        ('current_dc_component', 'Current DC component(1mA)'),
        ('voltage_dc_component', 'Voltage DC component (0.1V)'),
    )),
)
