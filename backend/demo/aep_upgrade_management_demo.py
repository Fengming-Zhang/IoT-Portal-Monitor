#!/usr/bin/python
# encoding=utf-8
import sys
sys.path.append('..')
import apis.aep_upgrade_management

if __name__ == '__main__':
    result = apis.aep_upgrade_management.QueryRemoteUpgradeDetail('dFI1lzE0EN2', 'xQcjrfNLvQ', 10015488, 'cd35c680b6d647068861f7fd4e79d3f5')
    print('result='+str(result))

    result = apis.aep_upgrade_management.QueryRemoteUpgradeTask('dFI1lzE0EN2', 'xQcjrfNLvQ', 10015488, 'cd35c680b6d647068861f7fd4e79d3f5')
    print('result='+str(result))

    result = apis.aep_upgrade_management.ControlRemoteUpgradeTask('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', '{}')
    print('result='+str(result))

    result = apis.aep_upgrade_management.QueryRemoteUpradeDeviceList('dFI1lzE0EN2', 'xQcjrfNLvQ', '10015488', 'cd35c680b6d647068861f7fd4e79d3f5')
    print('result='+str(result))

    result = apis.aep_upgrade_management.DeleteRemoteUpgradeTask('dFI1lzE0EN2', 'xQcjrfNLvQ', 10015488, 'cd35c680b6d647068861f7fd4e79d3f5')
    print('result='+str(result))

    result = apis.aep_upgrade_management.QueryRemoteUpgradeTaskList('dFI1lzE0EN2', 'xQcjrfNLvQ', 10015488, 'cd35c680b6d647068861f7fd4e79d3f5')
    print('result='+str(result))

    result = apis.aep_upgrade_management.ModifyRemoteUpgradeTask('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', '{}')
    print('result='+str(result))

    result = apis.aep_upgrade_management.CreateRemoteUpgradeTask('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', '{}')
    print('result='+str(result))

    result = apis.aep_upgrade_management.OperationalRemoteUpgradeTask('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', '{}')
    print('result='+str(result))

    result = apis.aep_upgrade_management.QueryRemoteUpgradeSubtasks('dFI1lzE0EN2', 'xQcjrfNLvQ', 10015488, 'cd35c680b6d647068861f7fd4e79d3f5')
    print('result='+str(result))

