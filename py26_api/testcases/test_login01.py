import logging
import os
import unittest

from requests import Request

from common.handleconfig import conf
from common.handlepath import DATADIR
from common.handlerequests import SendRequest
from common.readexcel import ReadExcel
from library.ddt import ddt, data

case_file = os.path.join(DATADIR, "apicases.xlsx")


@ddt
class TestLogin(unittest.TestCase):
    excel = ReadExcel(case_file, "login")
    cases = excel.read_data()
    request = SendRequest()

    @data(*cases)
    def test_login(self, case):
        url = conf.get("env", "url") + case["url"]
        headers = eval(conf.get("env", "headers"))
        method = case["method"]
        data = eval(case["data"])
        expected = eval(case["expected"])
        row=case["case_id"]+1
        response = self.request.send(url=url, method=method, headers=headers, json=data)
        res = response.json()
        print(res)
        try:
            self.assertEqual(res["msg"], expected["msg"])
            self.assertEqual(res["code"], expected["code"])
        except AssertionError as e:
            logging.error("用例{}未通过".format(case["title"]))
            logging.exception(e)
            self.excel.write_data(row=row,colume=8,value="未通过")
            raise e
        else :
            self.excel.write_data(row=row, column=8, value="通过")
            logging.info("用例{}通过".format(case["title"]))