#!/usr/bin/python
# encoding=utf-8
import sys
sys.path.append('..')
import apis.usr

if __name__ == '__main__':
    result = apis.usr.SdkDownload('dFI1lzE0EN2', 'xQcjrfNLvQ')
    print('result='+str(result))

