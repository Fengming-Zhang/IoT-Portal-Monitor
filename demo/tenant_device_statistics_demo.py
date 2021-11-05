#!/usr/bin/python
# encoding=utf-8
import sys
sys.path.append('..')
import apis.tenant_device_statistics

if __name__ == '__main__':
    result = apis.tenant_device_statistics.QueryTenantDeviceCount('dFI1lzE0EN2', 'xQcjrfNLvQ')
    print('result='+str(result))

    result = apis.tenant_device_statistics.QueryTenantDeviceTrend('dFI1lzE0EN2', 'xQcjrfNLvQ')
    print('result='+str(result))

    result = apis.tenant_device_statistics.QueryTenantDeviceActiveCount('dFI1lzE0EN2', 'xQcjrfNLvQ')
    print('result='+str(result))

