#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Li Na

import xlrd
from common.public import *
from utils.operationYaml import OperationYaml
import json

class ExcelVarles1:
    caseID="测试用例ID"
    caseModel="模块"
    caseName="接口名称"
    caseUrl="请求地址"
    casePre="前置方法"
    method="请求方法"
    paramsType="请求参数类型"
    paramdata="请求参数"
    expect="期望结果"
    isRun="是否运行"
    headersdata="请求头"
    status_code="状态码"


class OperationExcel1:
    def getSheet(self):
        book=xlrd.open_workbook(filePath('data','api.xlsx'))
        return book.sheet_by_index(0)

    @property
    def getRows(self):
        '''获取总行数'''
        return self.getSheet().nrows

    @property
    def getCols(self):
        '''获取总列数'''
        return self.getSheet().ncols

    def getValue(self,row,col):
        return self.getSheet().cell_value(row,col)

    @property
    def getExcelDatas(self):
        datas=list()
        title=self.getSheet().row_values(0)
        #忽略首行
        for row in range(1,self.getSheet().nrows):
            row_values=self.getSheet().row_values(row)
            datas.append(dict(zip(title,row_values)))
        return datas

    def runs(self):
        '''获取可执行的测试用例'''
        run_list=[]
        for item in self.getExcelDatas:
            isRun=item[ExcelVarles1.isRun]
            if isRun=='y':
                run_list.append(item)
            else:pass
        return run_list

    def case_list(self):
        '''获取excel中所有测试用例'''
        cases=list()
        for item in self.getExcelDatas:
            cases.append(item)
        return cases

    def case_prev(self,casePrev):
        '''
        依据前置测试条件找到关联的前置测试用例
        :param casePrev:前置测试条件
        :return:
        '''
        for item in self.case_list():
            print(item.values())
            print('--------------')
            if casePrev in item.values():
                return item
        return None

    def prevHeaders(self,prevReault):
        '''
        替换被关联测试点的请求头变量的值
        :param prevReault:
        :return:
        '''
        for item in self.runs():
            headers=item[ExcelVarles1.headersdata]
            if '{token}' in headers:
                headers=str(headers).replace('{token}',prevReault)
                #headers数据类型是字符串需要替换成字典
                #print(type(headers))
                return json.loads(headers)


if __name__=='__main__':
    obj=OperationExcel1()
    #print(obj.prevHeaders('123'))
    print(obj.case_prev('login'))




