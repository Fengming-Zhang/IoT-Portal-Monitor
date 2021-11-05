#!/usr/bin/python
# encoding=utf-8
import sys
sys.path.append('..')
import apis.aep_device_command

if __name__ == '__main__':
    result = apis.aep_device_command.CreateCommand('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', '{}')
    print('result='+str(result))

    result = apis.aep_device_command.QueryCommandList('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', 10015488, '10015488test')
    print('result='+str(result))

    result = apis.aep_device_command.QueryCommand('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', 10015488, '10015488test')
    print('result='+str(result))

    result = apis.aep_device_command.CancelCommand('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', '{}')
    print('result='+str(result))

