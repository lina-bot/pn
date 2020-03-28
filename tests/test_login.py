#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Li Na

import pytest
from base.method import Requests
from utils.operationYaml import OperationYaml
import json

obj=Requests()
objYaml=OperationYaml()

@pytest.mark.parametrize('datas',objYaml.readYaml() )
def test_login(datas):
    r=obj.post(
        url=datas['url'],
        json=datas['data'])
    #print(r.text)
    #print(r.status_code)
    assert datas['expect'] in json.dumps(r.json(),ensure_ascii=False)

if __name__=='__main__':
    pytest.main(["-s","-v","test_login.py"])


