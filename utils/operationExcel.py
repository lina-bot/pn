#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Li Na

import xlrd
from common.public import *
from utils.operationYaml import OperationYaml

class ExcelVarles:
    caseID=0
    des=1
    url=2
    method=3
    data=4
    expect=5

    @property
    def getCaseID(self):
        return self.caseID

    @property
    def getDescription(self):
        return self.des

    @property
    def getUrl(self):
        return self.url

    @property
    def getMethod(self):
        return self.method

    @property
    def getData(self):
        return self.data

    @property
    def getExpect(self):
        return self.expect

class OperationExcel(OperationYaml):
    def getSheet(self):
        book=xlrd.open_workbook(filePath('data','books.xlsx'))
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

    def getCaseid(self,row):
        return self.getValue(row=row,col=ExcelVarles().getCaseID)

    def getUrl(self,row):
        url=self.getValue(row=row,col=ExcelVarles().getUrl)
        if '{bookID}' in url:
            return str(url).replace('{bookID}',readContent())
        else:
            return url

    def getExcept(self,row):
        return self.getValue(row=row, col=ExcelVarles().getExpect)

    def getMethod(self,row):
        return self.getValue(row=row, col=ExcelVarles().getMethod)

    def getData(self,row):
        return self.getValue(row=row, col=ExcelVarles().getData)

    def getJson(self,row):
        return self.dictYaml()[self.getData(row=row)]

if __name__=='__main__':
    obj=OperationExcel()
    # print(obj.getValue(2,1))
    # print(obj.getValue(2,ExcelVarles().getDescription()))
    print(obj.getCaseid(row=2))
    print(obj.getUrl(row=2))
    print(obj.getExcept(row=2))
    print(obj.getMethod(row=2))
    print(obj.getJson(row=2))
    #<class 'dict'>字典类型就是想要的，不需要额外序列化
    print(type(obj.getJson(row=2)))


