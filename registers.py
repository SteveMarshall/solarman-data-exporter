# MODBUS Registers, prometheus name and description

all_regs = (
    (33022, (
        ('system_year', 'System Year(0-99)'),
        ('system_month', 'System Month'),
        ('system_day', 'System Day'),
        ('system_hour', 'System Hour'),
        ('system_minute', 'System Minute'),
        ('system_second', 'System Second'),
        ('not_used', 'Not Used'),
        ('total_generation_1', 'Total Generation 1(kWh)'),
        ('total_generation_2', 'Total Generation 2(kWh)'),
        ('generated_this_month_1', 'Generated This Month 1(kWh)'),
        ('generated_this_month_2', 'Generated This Month 2(kWh)'),
        ('generated_last_month_1', 'Generated Last Month 1(kWh)'),
        ('generated_last_month_2', 'Generated Last Month 2(kWh)'),
        ('generated_today', 'Generated Today(0.1kWh)'),
        ('generated_yesterday', 'Generated Yesterday(0.1kWh)'),
        ('generated_this_year_1', 'Generated This Year 1(kWh)'),
        ('generated_this_year_2', 'Generated This Year 2(kWh)'),
        ('generated_last_year_1', 'Generated Last Year 1(kWh)'),
        ('generated_last_year_2', 'Generated Last Year 2(kWh)'))),
    (33049, (
        ('dc_voltage_1', 'DC Voltage 1(0.1V)'),
        ('dc_current_1', 'DC Current 1(0.1A)'),
        ('dc_voltage_2', 'DC Voltage 2(0.1V)'),
        ('dc_current_2', 'DC Current 2(0.1A)'),
        ('dc_voltage_3', 'DC Voltage 3(0.1V)'),
        ('dc_current_3', 'DC Current 3(0.1A)'),
        ('dc_voltage_4', 'DC Voltage 4(0.1V)'),
        ('dc_current_4', 'DC Current 4(0.1A)'),
        ('total_dc_input_power_1', 'Total DC Input Power 1(W)'),
        ('total_dc_input_power_2', 'Total DC Input Power 2(W)'))),
    (33071, (
        ('dc_bus_voltage', 'DC bus Voltage(0.1V)'),
        ('dc_bus_half_voltage', 'DC bus half Voltage(0.1V)'),
        ('phase_a_voltage', 'Phase A Voltage(0.1V)'),
        ('phase_b_voltage', 'Phase B Voltage(0.1V)'),
        ('phase_c_voltage', 'Phase C Voltage(0.1V)'),
        ('phase_a_current', 'Phase A Current(0.1A)'),
        ('phase_b_current', 'Phase B Current(0.1A)'),
        ('phase_c_current', 'Phase C Current(0.1A)'),
        ('active_power_1', 'Active Power 1(W)'),
        ('active_power_2', 'Active Power 2(W)'),
        ('reactive_power_1', 'Reactive power 1(W)'),
        ('reactive_power_2', 'Reactive power 2(W)'),
        ('apparent_power_1', 'Apparent Power 1(VA)'),
        ('apparent_power_2', 'Apparent Power 2(VA)'))),
    (33091, (
        ('standard_working_mode', 'Standard Working Mode'),
        ('national_standard', 'National Standard'),
        ('inverter_temperature', 'Inverter Temperature(0.1C)'),
        ('grid_frequency', 'Grid Frequency(0.01Hz'),
        ('current_state_of_inverter', 'Current State Of Inverter'))),
    (33100, (
        ('limit_active_power_output_value_1', 'Limit Active Power Output 1(W)'),
        ('limit_active_power_output_value_2', 'Limit Active Power Output 2(W)'),
        ('limit_reactive_power_output_value_1', 'Limit Reactive Power Output 1(W)'),
        ('limit_reactive_power_output_value_2', 'Limit Reactive Power Output 2(W)'),
        ('actual_power_limited_power', 'Actual Power Limited Power(%)'),
        ('actual_adjustment_value', 'Actual Adjustment(0.001)'),
        ('limit_reactive_power_value', 'Limit Reactive Power(%)'))),
    (33126, (
        ('meter_total_energy_1', 'Electricity Meter Total Energy 1(Wh)'),
        ('meter_total_energy_2', 'Electricity Meter Total Energy 2(Wh)'),
        ('meter_voltage', 'Meter Voltage(0.1V)'),
        ('meter_current', 'Meter Current(0.1A)'),
        ('meter_active_power_1', 'Meter Active Power 1(0.1W)'),
        ('meter_active_power_2', 'Meter Active Power 2(0.1W)'),
        ('energy_storage_mode', 'Energy Storage Mode'),
        ('battery_voltage', 'Battery Voltage(0.1V)'),
        ('battery_current', 'Battery Current(0.1A)'),
        ('battery_current_direction', 'Battery Current_Direction(0=Charging, 1=Discharging'),
        ('llcbus_voltage', 'LLCbus Voltage(0.1V)'),
        ('bypass_ac_voltage', 'Bypass AC Voltage(0.1V)'),
        ('bypass_ac_current', 'Bypass AC Current(0.1A)'),
        ('battery_capacity_soc', 'Battery Capacity SOC(%)'),
        ('battery_health_soh', 'Battery Health SOH(%)'),
        ('battery_voltage', 'Battery Voltage(0.01V)'),
        ('battery_current', 'Battery Current(0.01A)'),
        ('battery_charge_current_limit', 'Battery Charge Current Limit(0.1A)'),
        ('battery_discharge_current_limit', 'Battery Discharge Current Limit(0.1A)'),
        ('battery_failure_info_01', 'Battery Failure Information 01'),
        ('battery_failure_info_02', 'Battery Failure Information 02'),
        ('house_load_power', 'House Load Power(W)'),
        ('bypass_load_power', 'Bypass Load Power(W)'),
        ('battery_power_1', 'Battery Power 1(W)'),
        ('battery_power_2', 'Battery Power 2(W)'))),
    (33161, (
        ('total_battery_charge_1', 'Total Battery Charge 1(kWh)'),
        ('total_battery_charge_2', 'Total Battery Charge 2(kWh)'),
        ('battery_charge_today', 'Battery Charge Today(0.1kWh)'),
        ('battery_charge_yesterday', 'Battery Charge Yesterday(0.1kWh)'),
        ('total_battery_discharge_1', 'Total Battery Discharge 1(kWh)'),
        ('total_battery_discharge_2', 'Total Battery Discharge 2(kWh)'),
        ('battery_discharge_capacity', 'Battery Discharge Capacity(0.1kWh)'),
        ('battery_discharge_power_yesterday', 'Battery Discharge Power Yesterday(0.1kWh)'),
        ('total_imported_energy_1', 'Total Imported Energy 1(kWh)'),
        ('total_imported_energy_2', 'Total Imported Energy 2(kWh)'),
        ('today_imported_energy', 'Today Imported Energy(0.1kWh)'),
        ('yesterday_imported_energy', 'Yesterday Imported Energy(0.1kWh)'),
        ('total_exported_energy_1', 'Total Exported Energy 1(kWh)'),
        ('total_exported_energy_2', 'Total Exported Energy 2(kWh)'),
        ('today_exported_energy', 'Today Exported Energy(0.1kWh)'),
        ('yesterday_exported_energy', 'Yesterday Exported Energy(0.1kWh)'),
        ('total_house_load_1', 'Total House Load 1(kWh)'),
        ('total_house_load_2', 'Total House Load 2(kWh)'),
        ('today_house_load', 'Today House Load(0.1kWh)'),
        ('yesterday_house_load', 'Yesterday House Load(0.1kWh)'))),
    (33251, (
        ('meter_ac_voltage_a', 'Meter AC Voltage A(0.1V)'),
        ('meter_ac_current_a', 'Meter AC Current A(0.01A)'),
        ('meter_ac_voltage_b', 'Meter AC Voltage B(0.1V)'),
        ('meter_ac_current_b', 'Meter AC Current B(0.01A)'),
        ('meter_ac_voltage_c', 'Meter AC Voltage C(0.1V)'),
        ('meter_ac_current_c', 'Meter AC Current C(0.01A)'),
        ('meter_active_power_a_1', 'Meter Active Power A 1(0.001kW)'),
        ('meter_active_power_a_2', 'Meter Active Power A 2(0.001kW)'),
        ('meter_active_power_b_1', 'Meter Active Power B 1(0.001kW)'),
        ('meter_active_power_b_2', 'Meter Active Power B 2(0.001kW)'),
        ('meter_active_power_c_1', 'Meter Active Power C 1(0.001kW)'),
        ('meter_active_power_c_2', 'Meter Active Power C 2(0.001kW)'),
        ('meter_total_active_power_1', 'Meter Total active Power 1(0.001kW)'),
        ('meter_total_active_power_2', 'Meter Total active Power 2(0.001kW)'),
        ('meter_reactive_power_a_1', 'Meter Active Reactive Power A 1(VA)'),
        ('meter_reactive_power_a_2', 'Meter Active Reactive Power A 2(VA)'),
        ('meter_reactive_power_b_1', 'Meter Active Reactive Power B 1(VA)'),
        ('meter_reactive_power_b_2', 'Meter Active Reactive Power B 2(VA)'),
        ('meter_reactive_power_c_1', 'Meter Active Reactive Power C 1(VA)'),
        ('meter_reactive_power_c_2', 'Meter Active Reactive Power C 2(VA)'),
        ('meter_total_reactive_power_1', 'Meter Total Reactive Power 1(VA)'),
        ('meter_total_reactive_power_2', 'Meter Total Reactive Power 2(VA)'),
        ('meter_apparent_power_a_1', 'Meter Active Apparent Power A 1(VA)'),
        ('meter_apparent_power_a_2', 'Meter Active Apparent Power A 2(VA)'),
        ('meter_apparent_power_b_1', 'Meter Active Apparent Power B 1(VA)'),
        ('meter_apparent_power_b_2', 'Meter Active Apparent Power B 2(VA)'),
        ('meter_apparent_power_c_1', 'Meter Active Apparent Power C 1(VA)'),
        ('meter_apparent_power_c_2', 'Meter Active Apparent Power C 2(VA)'),
        ('meter_total_apparent_power_1', 'Meter Total Apparent Power 1(VA)'),
        ('meter_total_apparent_power_2', 'Meter Total Apparent Power 2(VA)'),
        ('meter_power_factor', 'Meter Power Factor'),
        ('meter_grid_frequency', 'Meter Grid Frequency(0.01Hz)'),
        ('meter_total_active_imported_1', 'Meter Total Active Imported 1(0.01kWh)'),
        ('meter_total_active_imported_2', 'Meter Total Active Imported 2(0.01kWh)'),
        ('meter_total_active_exported_1', 'Meter Total Active Exported 1(0.01kWh)'),
        ('meter_total_active_exported_2', 'Meter Total Active Exported 2(0.01kWh)')))
        )


# For future
'''
(33115, (
    ('set_the_flag_bit', 'Set The Flag Bit'),
    ('fault_code_01', 'Fault Code 01'),
    ('fault_code_02', 'Fault Code 02'),
    ('fault_code_03', 'Fault Code 03'),
    ('fault_code_04', 'Fault Code 04'),
    ('fault_code_05', 'Fault Code 05'),
    ('working_status', 'Working Status'))),
'''