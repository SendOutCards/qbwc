# QBWC

QuickBooks Web Connector SDK (unofficial)

NOTE: WIP

## Basic Installation and Usage

```bash
virtualenv -p python3.7 env
./env/bin/pip install qbwc
QBWC_USER=user QBWC_PASSWORD=password QBWC_HOST=http://host.com QBWC_PORT=8166 ./env/bin/python
```

```python
>>> import qbwc
>>> qbwc.check.query(max_returned=5)
[{'txn_ID': '123A45-1234567890', 'time_created': datetime.datetime(2010, 2, 8 ...
```