#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Li Na

from base.method import Requests
from utils.operationExcel1 import *
import pytest
import json

excel = OperationExcel1()
obj = Requests()

@pytest.mark.parametrize('datas',excel.runs())
def test_login_book(datas):
    print(datas[ExcelVarles1.caseUrl])

    '''对请求参数反序列化处理：str变为字典'''
    param = datas[ExcelVarles1.paramdata]
    print('111',type(param))
    if len(str(param).strip()) == 0:pass
    elif len(str(param).strip()) > 0:
        param = json.loads(param)

    '''对请求头做反序列化的处理：str变为字典'''
    header=datas[ExcelVarles1.headersdata]
    if len(str(header).strip())==0:pass
    elif len(str(header).strip())>0:
        header=json.loads(header)
        #print('header',header)

    '''
    1. 获取到所有前置测试点的测试用例
    2. 执行前置测试点
    3. 获取他的结果信息
    4. 拿到它的结果信息替换对应测试点的变量
    '''

    #执行前置条件关联的测试点，执行对应接口把响应结果拿到
    r=obj.post(
        url=excel.case_prev(datas[ExcelVarles1.casePre])[ExcelVarles1.caseUrl],
        json=json.loads(excel.case_prev(datas[ExcelVarles1.casePre])[ExcelVarles1.paramdata]))
    prevResult=r.json()['access_token']

    #拿到响应结果，替换被测关联测试点中请求头信息的变量
    header=excel.prevHeaders(prevResult)

    #处理状态码
    status_code=int(datas[ExcelVarles1.status_code])

    def case_assert_result(r):
        assert r.status_code==status_code
        assert datas[ExcelVarles1.expect] in json.dumps(r.json(), ensure_ascii=False)

    if datas[ExcelVarles1.method]=='get':
        r=obj.get(url=datas[ExcelVarles1.caseUrl],
                  header=header)
        case_assert_result(r=r)
    elif datas[ExcelVarles1.method]=='post':
        r=obj.post(url=datas[ExcelVarles1.caseUrl],
                  json=param,
                  header=header)
        writeContent(content=str(r.json()[0]['datas']['id']))
        case_assert_result(r=r)
    elif datas[ExcelVarles1.method]=='delete':
        url=str(datas[ExcelVarles1.caseUrl]).replace('{bookID}',readContent())
        r=obj.delete(url=url,header=header)
        case_assert_result(r=r)

if __name__=='__main__':
    pytest.main(["-s","-v","test_login_token_book.py"])