#!/usr/bin/python
# encoding=utf-8
import sys
sys.path.append('..')
import apis.aep_rule_engine

if __name__ == '__main__':
    result = apis.aep_rule_engine.saasCreateRule('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_rule_engine.saasQueryRule('dFI1lzE0EN2', 'xQcjrfNLvQ', '10015488')
    print('result='+str(result))

    result = apis.aep_rule_engine.saasUpdateRule('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_rule_engine.saasDeleteRuleEngine('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_rule_engine.CreateRule('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_rule_engine.UpdateRule('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_rule_engine.DeleteRule('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_rule_engine.GetRules('dFI1lzE0EN2', 'xQcjrfNLvQ', '10015488')
    print('result='+str(result))

    result = apis.aep_rule_engine.GetRuleRunStatus('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_rule_engine.UpdateRuleRunStatus('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_rule_engine.CreateForward('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_rule_engine.UpdateForward('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_rule_engine.DeleteForward('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_rule_engine.GetForwards('dFI1lzE0EN2', 'xQcjrfNLvQ', '10015488')
    print('result='+str(result))

    result = apis.aep_rule_engine.GetWarns('dFI1lzE0EN2', 'xQcjrfNLvQ')
    print('result='+str(result))

    result = apis.aep_rule_engine.DeleteWarn('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_rule_engine.UpdateWarn('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_rule_engine.CreateWarn('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_rule_engine.CreateAction('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_rule_engine.UpdateAction('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_rule_engine.DeleteAction('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_rule_engine.GetActions('dFI1lzE0EN2', 'xQcjrfNLvQ')
    print('result='+str(result))

    result = apis.aep_rule_engine.GetWarnUsers('dFI1lzE0EN2', 'xQcjrfNLvQ')
    print('result='+str(result))

