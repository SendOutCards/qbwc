from functools import partial

from qbwc.base import query, mod

query = partial(query, 'check')
mod = partial(mod, 'check')
