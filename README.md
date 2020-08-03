# QBWC

QuickBooks Web Connector SDK (unofficial)

NOTE: WIP

## Basic Installation and Usage

```bash
virtualenv -p python3.7 env
./env/bin/pip install qbwc
QBWC_USER=user QBWC_PASSWORD=password QBWC_HOST=http://host.com QBWC_PORT=8166 ./env/bin/python
```

### One Request

```python
>>> import qbwc
>>> qbwc.rq({'CheckQueryRq': {'MaxReturned': 5}})
{'CheckQueryRs': {'CheckRet': [<Check>, <Check>]}}
```

### Two Requests of the Same Type

```python
>>> import qbwc
>>> qbwc.rq({'CheckQueryRq': [
	{'TxnDateRangeFilter': {'DateMacro': 'ThisWeek'}},
	{'TxnDateRangeFilter': {'DateMacro': 'LastWeek'}}
]})
{'CheckQueryRs': [{'CheckRet': [<Check>, <Check>]}, {'CheckRet': [<Check>, <Check>]}]}
```

### Two Requests of the Different Types

```python
>>> import qbwc
>>> qbwc.rq({
	'CheckQueryRq': {
		'TxnDateRangeFilter': {'DateMacro': 'ThisWeek'}
	},
	'PurchaseOrderQueryRq': {
		'ItemInventoryQueryRq': {
        	'ActiveStatus': 'ActiveOnly'
    	}
    }
})
{'CheckQueryRs': [{'CheckRet': [<Check>, <Check>]}],
 'PurchaseOrderQueryRs': [{'PurchaseOrderRet': [<PurchaseOrder>, <PurchaseOrder>, <etc>]}]
```


## API

For now, see:

1. `qbwc/generated/types.py` ending with Rq to learn how to construct requests. Includes all supported `Enum` types and all cases of `Union[val, List[val]]` where a param can be repeated.
2. `data/json/*.json` for Rq documentation showing nested params in a json format.
3. `data/xml/*.xml` documentation scraped and reconstructed from https://developer.intuit.com/app/developer/qbdesktop/docs/api-reference. Also, used to generate python types.

_NOTE: In XML, comments that read `<!-- options|required|may repeat -->` apply to param immediately above. Comments that read <!-- 