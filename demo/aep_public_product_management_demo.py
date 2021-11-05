#!/usr/bin/python
# encoding=utf-8
import sys
sys.path.append('..')
import apis.aep_public_product_management

if __name__ == '__main__':
    result = apis.aep_public_product_management.QueryPublicByPublicProductId('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_public_product_management.QueryPublicByProductId('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_public_product_management.InstantiateProduct('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_public_product_management.QueryAllPublicProductList('dFI1lzE0EN2', 'xQcjrfNLvQ')
    print('result='+str(result))

    result = apis.aep_public_product_management.QueryMyPublicProductList('dFI1lzE0EN2', 'xQcjrfNLvQ')
    print('result='+str(result))

