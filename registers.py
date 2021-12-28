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
        ('dc_current_2', 'DC Current 2(0.1A)'))),
    (33057, (
        ('total_dc_output_power_1', 'Total DC Output Power 1(W)'),
        ('total_dc_output_power_2', 'Total DC Output Power 2(W)'))),
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
    (33104, (
        ('actual_power_limit', 'Actual Power Limit(0.01%)'),
        ('actual_power', 'Actual Power(0.01)'))),
    (33126, (
        ('electricity_meter_total_active_power_generation_1', 'Electricity Meter Total Active Power Generation 1(Wh)'),
        ('electricity_meter_total_active_power_generation_2', 'Electricity Meter Total Active Power Generation 2(Wh)'),
        ('meter_voltage', 'Meter Voltage(0.1V)'),
        ('meter_current', 'Meter Current(0.1A)'),
        ('meter_active_power_1', 'Meter Active Power 1(0.1W)'),
        ('meter_active_power_2', 'Meter Active Power 2(0.1W)'),
        ('energy_storage_control_switch', 'Energy Storage Control Switch'),
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
        ('total_imported_power_1', 'Total Imported Power 1(kWh)'),
        ('total_imported_power_2', 'Total Imported Power 2(kWh)'),
        ('grid_power_imported_today', 'Grid Power Imported Today(0.1kWh)'),
        ('grid_power_imported_yesterday', 'Grid Power Imported Yesterday(0.1kWh)'),
        ('total_exported_power_1', 'Total Exported Power 1(kWh)'),
        ('total_exported_power_2', 'Total Exported Power 2(kWh)'),
        ('grid_power_exported_today', 'Grid Power Exported Today(0.1kWh)'),
        ('grid_power_exported_yesterday', 'Grid Power Exported Yesterday(0.1kWh)'),
        ('total_house_load_1', 'Total House Load 1(kWh)'),
        ('total_house_load_2', 'Total House Load 2(kWh)'),
        ('house_load_today', 'House Load Today(0.1kWh)'),
        ('house_load_yesterday', 'House Load Yesterday(0.1kWh)'))),
    (33251, (
        ('meter_ac_voltage_a', 'Meter AC Voltage A(0.1V)'),
        ('meter_ac_current_a', 'Meter AC Current A(0.01A)'),
        ('meter_ac_voltage_b', 'Meter AC Voltage B(0.1V)'),
        ('meter_ac_current_b', 'Meter AC Current B(0.01A)'),
        ('meter_ac_voltage_c', 'Meter AC Voltage C(0.1V)'),
        ('meter_ac_current_c', 'Meter AC Current C(0.01A)'),
        ('meter_active_power_a', 'Meter Active Power A(0.001kW)'),
        ('not_used', 'Not Used'),
        ('meter_active_power_b', 'Meter Active Power B(0.001kW)'),
        ('not_used', 'Not Used'),
        ('meter_active_power_c', 'Meter Active Power C(0.001kW)'),
        ('not_used', 'Not Used'),
        ('meter_total_active_power', 'Meter Total active Power(0.001kW)'),
        ('not_used', 'Not Used'),
        ('meter_reactive_power_a', 'Meter Active Reactive Power A(VA)'),
        ('not_used', 'Not Used'),
        ('meter_reactive_power_b', 'Meter Active Reactive Power B(VA)'),
        ('not_used', 'Not Used'),
        ('meter_reactive_power_c', 'Meter Active Reactive Power C(VA)'),
        ('not_used', 'Not Used'),
        ('meter_total_reactive_power', 'Meter Total Reactive Power(VA)'),
        ('not_used', 'Not Used'),
        ('meter_apparent_power_a', 'Meter Active Apparent Power A(VA)'),
        ('not_used', 'Not Used'),
        ('meter_apparent_power_b', 'Meter Active Apparent Power B(VA)'),
        ('not_used', 'Not Used'),
        ('meter_apparent_power_c', 'Meter Active Apparent Power C(VA)'),
        ('not_used', 'Not Used'),
        ('meter_total_apparent_power', 'Meter Total Apparent Power(VA)'),
        ('not_used', 'Not Used'),
        ('meter_power_factor', 'Meter Power Factor'),
        ('meter_grid_frequency', 'Meter Grid Frequency(0.01Hz)'),
        ('meter_total_active_imported', 'Meter Total Active Imported (0.01kWh)'),
        ('not_used', 'Not Used'),
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