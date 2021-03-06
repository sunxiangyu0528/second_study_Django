import logging
import os
import unittest
import jsonpath

from common.connectdb import DB
from common.handle_data import CaseDate
from common.handleconfig import conf
from common.handlepath import DATADIR
from common.handlerequests import SendRequest
from common.readexcel import ReadExcel
from library.ddt import ddt, data

case_file = os.path.join(DATADIR, "apicases.xlsx")


@ddt
class TestRechage01(unittest.TestCase):
    request = SendRequest()
    excel = ReadExcel(case_file, "recharge")
    cases = excel.read_data()
    db=DB()

    @classmethod
    def setUpClass(cls) -> None:
        url = conf.get("env", "url") + "/member/login"
        method = "post"
        headers = eval(conf.get("env", "headers"))
        data = {
            "mobile_phone": conf.get("test_data", "phone"),
            "pwd": conf.get("test_data", "pwd")
        }
        response = cls.request.send(url=url, headers=headers, method=method, json=data)
        res = response.json()
        print(res)
        # 提取token
        token_type = jsonpath.jsonpath(res, "$..token_type")[0]
        print(token_type)
        token = jsonpath.jsonpath(res, "$..token")[0]
        print(token)
        cls.token_value = token_type + " " + token
        cls.member_id = str(jsonpath.jsonpath(res, "$..id")[0])

    @data(*cases)
    def test_rechage(self, case):
        url = conf.get("env", "url") + case["url"]
        method = case["method"]
        case["data"] = case["data"].replace("#member_id#", self.member_id)
        data = eval(case["data"])
        headers = eval(conf.get("env","headers"))
        headers["Authorization"] = self.token_value
        print(headers)
        row = case["case_id"] + 1
        expected = eval(case["expected"])
        response = self.request.send(url=url, method=method, json=data, headers=headers)
        res = response.json()
        if case["check_sql"]:
            sql="SELECT leave_amount FROM futureloan.member WHERE mobile_phone={}".format(conf.get("test_data", "phone"))
            self.db.find_one(sql)


        try:
            self.assertEqual(res["code"], expected["code"])
            self.assertEqual(res["code"], expected["code"])
        except AssertionError as e:
            logging.error(e)
            logging.exception(e)
            self.excel.write_data(row=row, column=8, value="未通过")
            raise e
        else:
            self.excel.write_data(row=row, column=8, value="通过")


if __name__ == "__main__":
    unittest.main()
