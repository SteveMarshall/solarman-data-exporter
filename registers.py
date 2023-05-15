from collections import namedtuple
import logging
from pysolarmanv5.pysolarmanv5 import PySolarmanV5

Register = namedtuple(
    'Register',
    'label description'
)

Metric = namedtuple('Metric', Register._fields + ('value',))

class RegisterSet(namedtuple('RegisterSet', 'address registers')):
    __slots__ = ()

    def _read_values(self, modbus: PySolarmanV5):
        logging.debug(f'Reading {self}')
        return modbus.read_holding_registers(
            self.address,
            len(self.registers)
        )

    def read_metrics(self, modbus: PySolarmanV5):
        values = self._read_values(modbus)
        return [
            Metric(register.label, register.description, value)
            for (register, value) in zip(self.registers, values)
        ]

class FormattedRegisterSet(namedtuple(
    'FormattedRegisterSet',
    RegisterSet._fields + ('register_size',),
    defaults=(1,)
), RegisterSet):
    __slots__ = ()

    def _read_values(self, modbus: PySolarmanV5):
        logging.debug(f'Reading {self}')
        return [
            modbus.read_holding_register_formatted(
                sub_address,
                self.register_size
            )
            for sub_address in range(
                self.address,
                self.address + (self.register_size * len(self.registers)),
                self.register_size
            )
        ]
