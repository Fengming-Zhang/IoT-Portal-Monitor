#!/usr/bin/python
# encoding=utf-8
import sys
sys.path.append('..')
import apis.tenant_app_statistics

if __name__ == '__main__':
    result = apis.tenant_app_statistics.QueryTenantApiMonthlyCount('dFI1lzE0EN2', 'xQcjrfNLvQ')
    print('result='+str(result))

    result = apis.tenant_app_statistics.QueryTenantAppCount('dFI1lzE0EN2', 'xQcjrfNLvQ')
    print('result='+str(result))

    result = apis.tenant_app_statistics.QueryTenantApiTrend('dFI1lzE0EN2', 'xQcjrfNLvQ')
    print('result='+str(result))

