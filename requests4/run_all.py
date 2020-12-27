'''组织执行用例'''
import time
import unittest
from BeautifulReport import BeautifulReport
from setting import CASE_PATH, REPORT_PATH

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

#unittest的discover批量执行testcase，这里面有三个参数，
discover = unittest.defaultTestLoader.discover(start_dir=CASE_PATH,        #分别是用例所在目录
                                               pattern='test_login2.py',   #执行的用例名称
                                               top_level_dir=None)         #是否有顶级目录
time_str = time.strftime("%Y%m%d%H%M%S")   #获取当时时间年月日时分秒
filename ="report-"+time_str+".html"      #字符串拼接得到生成的报告名字，并赋给filename
br = BeautifulReport(discover)            #实例化
br.report(description="小白接口自动化测试报告", #用到BeautifulReport()的方法.report，这里三个参数分别是：报告的描述
          filename=filename,       #生成报告的名称
          log_path=REPORT_PATH)    #生成报告的路径
