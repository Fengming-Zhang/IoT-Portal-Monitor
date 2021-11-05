#!/usr/bin/python
# encoding=utf-8
import sys
sys.path.append('..')
import apis.aep_mq_sub

if __name__ == '__main__':
    result = apis.aep_mq_sub.QueryServiceState('dFI1lzE0EN2', 'xQcjrfNLvQ')
    print('result='+str(result))

    result = apis.aep_mq_sub.OpenMqService('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_mq_sub.CreateTopic('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_mq_sub.QueryTopicInfo('dFI1lzE0EN2', 'xQcjrfNLvQ')
    print('result='+str(result))

    result = apis.aep_mq_sub.QueryTopicCacheInfo('dFI1lzE0EN2', 'xQcjrfNLvQ')
    print('result='+str(result))

    result = apis.aep_mq_sub.QueryTopics('dFI1lzE0EN2', 'xQcjrfNLvQ')
    print('result='+str(result))

    result = apis.aep_mq_sub.ChangeTopicInfo('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_mq_sub.QuerySubRules('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_mq_sub.ChangeSubRules('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_mq_sub.ClosePushService('dFI1lzE0EN2', 'xQcjrfNLvQ')
    print('result='+str(result))

