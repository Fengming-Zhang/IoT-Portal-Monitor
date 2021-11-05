#!/usr/bin/python
# encoding=utf-8
import sys
sys.path.append('..')
import apis.aep_device_model

if __name__ == '__main__':
    result = apis.aep_device_model.QueryPropertyList('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', 10015488)
    print('result='+str(result))

    result = apis.aep_device_model.QueryServiceList('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', 10015488)
    print('result='+str(result))

