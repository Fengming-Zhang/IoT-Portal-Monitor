#!/usr/bin/python
# encoding=utf-8
import sys
sys.path.append('..')
import apis.aep_nb_device_management

if __name__ == '__main__':
    result = apis.aep_nb_device_management.BatchCreateNBDevice('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_nb_device_management.BatchCancelDevices('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', '{}')
    print('result='+str(result))

