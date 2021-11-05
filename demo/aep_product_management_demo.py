#!/usr/bin/python
# encoding=utf-8
import sys
sys.path.append('..')
import apis.aep_product_management

if __name__ == '__main__':
    result = apis.aep_product_management.QueryProduct('dFI1lzE0EN2', 'xQcjrfNLvQ', 10015488)
    print('result='+str(result))

    result = apis.aep_product_management.QueryProductList('dFI1lzE0EN2', 'xQcjrfNLvQ')
    print('result='+str(result))

    result = apis.aep_product_management.DeleteProduct('dFI1lzE0EN2', 'xQcjrfNLvQ', 'cd35c680b6d647068861f7fd4e79d3f5', 10015488)
    print('result='+str(result))

    result = apis.aep_product_management.CreateProduct('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_product_management.UpdateProduct('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

