#!/usr/bin/python
# encoding=utf-8
import sys
sys.path.append('..')
import apis.aep_firmware_management

if __name__ == '__main__':
    result = apis.aep_firmware_management.UpdateFirmware('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', '{}')
    print('result='+str(result))

    result = apis.aep_firmware_management.QueryFirmwareList('dFI1lzE0EN2', 'xQcjrfNLvQ', 10015488, 'cd35c680b6d647068861f7fd4e79d3f5')
    print('result='+str(result))

    result = apis.aep_firmware_management.QueryFirmware('dFI1lzE0EN2', 'xQcjrfNLvQ', 10015488, 'cd35c680b6d647068861f7fd4e79d3f5')
    print('result='+str(result))

    result = apis.aep_firmware_management.DeleteFirmware('dFI1lzE0EN2', 'xQcjrfNLvQ', 10015488, 'cd35c680b6d647068861f7fd4e79d3f5')
    print('result='+str(result))

