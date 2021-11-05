#!/usr/bin/python
# encoding=utf-8
import sys
sys.path.append('..')
import apis.aep_device_group_management

if __name__ == '__main__':
    result = apis.aep_device_group_management.CreateDeviceGroup('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', '{}')
    print('result='+str(result))

    result = apis.aep_device_group_management.UpdateDeviceGroup('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', '{}')
    print('result='+str(result))

    result = apis.aep_device_group_management.DeleteDeviceGroup('dFI1lzE0EN2', 'xQcjrfNLvQ', 10015488, 'cd35c680b6d647068861f7fd4e79d3f5')
    print('result='+str(result))

    result = apis.aep_device_group_management.QueryDeviceGroupList('dFI1lzE0EN2', 'xQcjrfNLvQ', 10015488, 'cd35c680b6d647068861f7fd4e79d3f5')
    print('result='+str(result))

    result = apis.aep_device_group_management.QueryGroupDeviceList('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', 10015488)
    print('result='+str(result))

    result = apis.aep_device_group_management.UpdateDeviceGroupRelation('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', '{}')
    print('result='+str(result))

    result = apis.aep_device_group_management.getGroupDetailByDeviceId('dFI1lzE0EN2', 'xQcjrfNLvQ', 10015488, '10015488test')
    print('result='+str(result))

