from functools import partial

from qbwc.base import query, mod

query = partial(query, 'purchase_order')
mod = partial(mod, 'purchase_order')
