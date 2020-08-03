from os import environ as env

user = env.get('QBWC_USER')
password = env.get('QBWC_PASSWORD')
port = env.get('QBWC_PORT', '8166')
host = env.get('QBWC_HOST')
uri = f'http://{user}:{password}@{host}:{port}'
request_headers = {
    'X-AcctSyncInteractionType': '0'
}
debug = env.get('DEBUG', 'False') in {'True', 'true', '1'}
_config_keys = {
    'user', 'password', 'port', 'host', 
    'uri', 'request_headers', 'debug'
}


def update(**kwargs):
    assert all(k in _config_keys for k in kwargs)
    globals().update(kwargs)