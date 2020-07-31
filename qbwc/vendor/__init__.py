from functools import partial

from qbwc.base import query, mod

query = partial(query, 'vendor')
mod = partial(mod, 'vendor')