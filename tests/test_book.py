#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Li Na

from base.method import Requests
from utils.operationYaml import OperationYaml
from utils.operationExcel import OperationExcel
import pytest
import json
from common.public import *

class TestBook:
    excel=OperationExcel()
    obj=Requests()

    def result(self,r,row):
        assert r.status_code == 200
        assert self.excel.getExcept(row=row) in json.dumps(r.json(), ensure_ascii=False)

    def test_book_001(self):
        '''获取所有书籍信息'''
        r=self.obj.get(url=self.excel.getUrl(row=1))
        self.result(r=r,row=1)

    def test_book_002(self):
        '''添加书籍'''
        r = self.obj.post(
            url=self.excel.getUrl(row=2),
            json=self.excel.getJson(row=2))
        print(r.text)
        self.result(r=r,row=2)
        #writeContent(content=r.json()[0]['datas']['id'])

    def test_book_003(self):
        '''查看书籍'''
        r = self.obj.get(url=self.excel.getUrl(row=1))
        print(r.url)
        self.result(r=r,row=3)

    def test_book_004(self):
        '''编辑书籍信息'''
        r=self.obj.put(
            url=self.excel.getUrl(row=4),
            json=self.excel.getJson(row=4))
        self.result(r=r,row=4)

    def test_book_005(self):
        '''删除书籍信息'''
        r=self.obj.delete(
            url=self.excel.getUrl(row=5))
        self.result(r=r,row=5)


if __name__=='__main__':
    pytest.main(['-s',"-v","test_book.py"])
    pytest.main(['-s', "-v", "test_book.py::TestBook::test_book_002"])