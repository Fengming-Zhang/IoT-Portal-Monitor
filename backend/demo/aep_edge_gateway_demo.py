#!/usr/bin/python
# encoding=utf-8
import sys
sys.path.append('..')
import apis.aep_edge_gateway

if __name__ == '__main__':
    result = apis.aep_edge_gateway.DeleteEdgeInstanceDevice('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_edge_gateway.QueryEdgeInstanceDevice('dFI1lzE0EN2', 'xQcjrfNLvQ')
    print('result='+str(result))

    result = apis.aep_edge_gateway.CreateEdgeInstance('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_edge_gateway.EdgeInstanceDeploy('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_edge_gateway.DeleteEdgeInstance('dFI1lzE0EN2', 'xQcjrfNLvQ')
    print('result='+str(result))

    result = apis.aep_edge_gateway.AddEdgeInstanceDevice('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_edge_gateway.AddEdgeInstanceDrive('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

