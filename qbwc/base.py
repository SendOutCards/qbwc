from datetime import datetime
from typing import Union, List, Optional, Set

from qbwc.common import (
    request, 
    except_on_mutually_exclusive_params,
    except_without_required_params
)
from qbwc.types import (
    ModifiedDateRangeFilter,
    TxnDateRangeFilter
)


def query(
    resource: str,
    txn_ID: Optional[Union[str, List[str]]]=None, 
    ref_number: Optional[Union[int, List[int]]]=None,
    ref_number_case_sensitive: Optional[Union[int, List[int]]]=None,
    max_returned: Optional[int]=None,
    modified_date_range_filter: Optional[ModifiedDateRangeFilter]=None,
    txn_date_range_filter: Optional[TxnDateRangeFilter]=None,
    **kwargs
) -> Union[dict, List[dict]]:
    """
    API Documentation:

    https://developer.intuit.com/app/developer/qbdesktop/docs/api-reference/qbdesktop
    """
    kwargs = {
        'txn_ID': txn_ID,
        'ref_number': ref_number,
        'ref_number_case_sensitive': ref_number_case_sensitive,
        'max_returned': max_returned,
        'modified_date_range_filter': modified_date_range_filter,
        'txn_date_range_filter': txn_date_range_filter,
        **kwargs
    }
    except_on_mutually_exclusive_params([{
        'txn_ID',
        'ref_number',
        'ref_number_case_sensitive',
        'max_returned'
    }, {
        'modified_date_range_filter',
        'txn_date_range_filter'
    }], kwargs)
    return request(f'{resource}_query', kwargs)


def mod(resource: str, objs: Union[dict, List[dict]], required: Set[str]=set(), minimum_additional_fields: str=0):
    except_without_required_params(
        required | {'txn_ID', 'edit_sequence'}, 
        minimum_additional_fields + 1,
        objs
    )
    return request(f'{resource}_mod', objs)
