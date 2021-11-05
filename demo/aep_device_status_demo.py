#!/usr/bin/python
# encoding=utf-8
import sys
sys.path.append('..')
import apis.aep_device_status

if __name__ == '__main__':
    result = apis.aep_device_status.QueryDeviceStatus('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_device_status.QueryDeviceStatusList('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_device_status.getDeviceStatusHisInTotal('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_device_status.getDeviceStatusHisInPage('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

