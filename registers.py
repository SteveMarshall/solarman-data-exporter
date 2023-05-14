from collections import namedtuple
from pysolarmanv5.pysolarmanv5 import PySolarmanV5

Register = namedtuple(
    'Register',
    'label description'
)
class RegisterSet(namedtuple('RegisterSet', 'address registers')):
    __slots__ = ()

    def read(self, modbus: PySolarmanV5):
        return modbus.read_holding_registers(
            self.address,
            len(self.registers)
        )

class FormattedRegisterSet(namedtuple(
    'FormattedRegisterSet',
    RegisterSet._fields + ('register_size',),
    defaults=(1,)
)):
    __slots__ = ()

    def read(self, modbus: PySolarmanV5):
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
