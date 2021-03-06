"""
============================
Author:柠檬班-木森
Time:2020/3/5   11:05
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import unittest
import os
from common.handlepath import REPORTDIR
from common.handle_email import send_email
from testcases import test_main_stream
from library.HTMLTestRunnerNew import HTMLTestRunner

suite = unittest.defaultTestLoader.loadTestsFromModule(test_main_stream)

report_file = os.path.join(REPORTDIR,"report11.html")

# 第三步：执行用例
runner = HTMLTestRunner(stream=open(report_file, "wb"),
                        description="接口项目主流程测试报告",
                        title="主流程测试报告",
                        tester="musen"
                        )

runner.run(suite)


send_email(report_file,"主流程测试报告")
print("123456789")