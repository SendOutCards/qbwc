# QBWC

QuickBooks Web Connector SDK (unofficial)

NOTE: WIP

## Development (WIP)

1. `make dev`
2. Make changes
3. `make test`
4. Manually test changes (see below) against a QBWC

```bash
QBWC_USER=user QBWC_PASSWORD=password QBWC_HOST=http://host.com QBWC_PORT=8166 ./env/bin/ipython
```

```python
import qbwc

<exercise code>
```



## Deploy

1. `make test`
2. Inc version in setup.py according to semantic versioning rules in it's own commit
3. Make PR and merge
4. Checkout master
5. `git tag <version in setup.py>`
6. `git push --tags` 
7. `cp .pypirc.example ~/.pypirc`
8. Edit `~/.pypirc`, populate `[soc]` section with credentials
9. `make deploy`
10. Done

## Basic Installation and Usage

```bash
make env
./env/bin/pip install -e .  # editable install
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