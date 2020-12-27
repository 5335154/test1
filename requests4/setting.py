import os

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

#顶层目录
DIR= os.path.dirname(os.path.abspath(__file__))

#data
DATA_PATH=os.path.join(DIR,'data')
#lib
LIB_PATH=os.path.join(DIR,'lib')
#test_case
CASE_PATH=os.path.join(DIR,'test_case')
#report
REPORT_PATH=os.path.join(DIR,'report')

