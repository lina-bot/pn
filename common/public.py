#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Li Na

import os,datetime

def filePath(fileDir='data',fileName='login.yaml'):
    '''
    :param fileDir:目录
    :param fileName:文件名称
    :return:
    '''

    return os.path.join(
        os.path.dirname(os.path.dirname(__file__)),fileDir,fileName)

def writeContent(content):
    print('写的时间',datetime.datetime.now())
    with open(filePath(fileDir='data',fileName='bookID'),'w') as f:
        f.write(str(content))
#writeContent('1')

def readContent():
    print('读的时间', datetime.datetime.now())
    with open(filePath(fileDir='data',fileName='bookID'),'r') as f:
        return f.read()

# print(filePath())
# print(filePath('config','config.yaml'))
# print(os.path.dirname(__file__))
# #print(os.path.join(base_url,'data','login.yaml'))
# #当前目录的上级目录
# print(os.path.dirname(os.path.dirname(__file__)))



