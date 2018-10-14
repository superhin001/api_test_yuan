#coding:utf-8
'''执行所有用例入口'''
import unittest
from  lib.HTMLTestRunner_PY3 import  HTMLTestRunner
from  lib.sand_email import send_report
from config import confing as cf

suite = unittest.defaultTestLoader.discover(cf.testcase_path)
with open(cf.report_file,'wb') as f:
    HTMLTestRunner(stream=f,
                   title="api test",
                   description="test").run(suite)

if cf.is_send_email:
     send_report()