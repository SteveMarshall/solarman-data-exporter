from collections import namedtuple
import logging
from pysolarmanv5.pysolarmanv5 import PySolarmanV5

Register = namedtuple(
    'Register',
    'label description size signed',
    defaults=(1, False)
)

Metric = namedtuple('Metric', 'label description value')

class RegisterSet(namedtuple('RegisterSet', 'address registers')):
    __slots__ = ()

    @property
    def size(self):
        return sum([
            register.size
            for register in self.registers
        ])

    def read_metrics(self, modbus: PySolarmanV5):
        logging.debug(f'Reading {self}')
        raw_values = modbus.read_holding_registers(
            self.address,
            self.size
        )

        value_start = 0
        for register in self.registers:
            logging.debug(f'Reading {register}')
            value_end = value_start + register.size
            yield Metric(
                register.label,
                register.description,
                modbus._format_response(
                    raw_values[value_start:value_end],
                    signed=register.signed
                )
            )
            value_start = value_end
