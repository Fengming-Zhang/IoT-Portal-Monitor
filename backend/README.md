# CTWingSKIT_BC28 Backend

## Environment

- python 3.8.8
- Webservice framework: flask

## Framework

```bash
-- backend/
---- apis/						// interface to access data and control of devices connected to AEP platform
---- demo/						// examples to show how to make use of each interface
---- docs/						// interface definition and arguments' illustration
---- monitor_service.py			// script to start the backend service
---- README.md
```

## Configuration

Config IDs and keys as authentication (available on the AEP platform)

```python
# product config
PRODUCT_ID = '15101463'
DEVICE_ID = '76afab91af78499582abc2b36c651cfc'
APP_KEY = 'TW8Xcu4tpfl'
APP_SECRET = '8KNtazD7Ae'
MASTER_API_KEY = '308fdaf1c5fb4ff1b020be995c54e26b'
```

## Start Service

```bash
cd ${repo-root}/backend/
python monitor_service.py
```

