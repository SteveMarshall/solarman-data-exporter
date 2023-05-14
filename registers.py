from collections import namedtuple

Register = namedtuple(
    'Register',
    'label description'
)
RegisterSet = namedtuple('RegisterSet', 'address registers')

FormattedRegisterSet = namedtuple(
    'FormattedRegisterSet',
    RegisterSet._fields + ('register_size',),
    defaults=(1,)
)
