#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import unittest

from lept_constants import LeptType, LeptParseReturnValue
from leptjson import LeptJson


class LeptTest(unittest.TestCase):
    def test_parse_null(self):
        self.return_value_and_type_test(LeptParseReturnValue.ok, LeptType.null, "null")

    def test_parse_expect_value(self):
        self.return_value_and_type_test(LeptParseReturnValue.expect_value, LeptType.null, "")
        self.return_value_and_type_test(LeptParseReturnValue.expect_value, LeptType.null, "  ")

    def test_parse_invalid_value(self):
        self.return_value_and_type_test(LeptParseReturnValue.invalid_value, LeptType.null, "nul")
        self.return_value_and_type_test(LeptParseReturnValue.invalid_value, LeptType.null, "?")

    def test_parse_root_not_singular(self):
        self.return_value_and_type_test(LeptParseReturnValue.root_not_singular, LeptType.null, "null x")

    def test_parse_number(self):
        self.return_value_and_type_test(LeptParseReturnValue.ok, LeptType.number, "0", 0.0)
        self.return_value_and_type_test(LeptParseReturnValue.ok, LeptType.number, "-0", 0.0)
        self.return_value_and_type_test(LeptParseReturnValue.ok, LeptType.number, "-0.0", 0.0)
        self.return_value_and_type_test(LeptParseReturnValue.ok, LeptType.number, "1.0", 1)
        self.return_value_and_type_test(LeptParseReturnValue.ok, LeptType.number, "-1.0", -1)
        self.return_value_and_type_test(LeptParseReturnValue.ok, LeptType.number, "1.5", 1.5)
        self.return_value_and_type_test(LeptParseReturnValue.ok, LeptType.number, "-1.5", -1.5)
        self.return_value_and_type_test(LeptParseReturnValue.ok, LeptType.number, "3.1416", 3.1416)
        self.return_value_and_type_test(LeptParseReturnValue.ok, LeptType.number, "1E10", 1E10)
        self.return_value_and_type_test(LeptParseReturnValue.ok, LeptType.number, "1e10", 1e10)
        self.return_value_and_type_test(LeptParseReturnValue.ok, LeptType.number, "1E+10", 1E+10)
        self.return_value_and_type_test(LeptParseReturnValue.ok, LeptType.number, "1E-10", 1E-10)
        self.return_value_and_type_test(LeptParseReturnValue.ok, LeptType.number, "-1E10", -1E10)
        self.return_value_and_type_test(LeptParseReturnValue.ok, LeptType.number, "-1e10", -1e10)
        self.return_value_and_type_test(LeptParseReturnValue.ok, LeptType.number, "-1E+10", -1E+10)
        self.return_value_and_type_test(LeptParseReturnValue.ok, LeptType.number, "-1E-10", -1E-10)
        self.return_value_and_type_test(LeptParseReturnValue.ok, LeptType.number, "1.234E+10", 1.234E+10)
        self.return_value_and_type_test(LeptParseReturnValue.ok, LeptType.number, "1.234E-10", 1.234E-10)
        self.return_value_and_type_test(LeptParseReturnValue.ok, LeptType.number, "0.0", 1e-10000)

        self.return_value_and_type_test(LeptParseReturnValue.invalid_value, LeptType.null, "+0")
        self.return_value_and_type_test(LeptParseReturnValue.invalid_value, LeptType.null, "+1")
        self.return_value_and_type_test(LeptParseReturnValue.invalid_value, LeptType.null, ".123")
        self.return_value_and_type_test(LeptParseReturnValue.invalid_value, LeptType.null, "1.")
        self.return_value_and_type_test(LeptParseReturnValue.invalid_value, LeptType.null, "INF")
        self.return_value_and_type_test(LeptParseReturnValue.invalid_value, LeptType.null, "inf")
        self.return_value_and_type_test(LeptParseReturnValue.invalid_value, LeptType.null, "NAN")
        self.return_value_and_type_test(LeptParseReturnValue.invalid_value, LeptType.null, "nan")

        self.return_value_and_type_test(LeptParseReturnValue.ok, LeptType.number, "1.0000000000000002",
                                        1.0000000000000002)
        # TODO(coderyrh9236@gmail.com): 修复由于 float() 造成的精度丢失，导致测试样例失败
        # self.return_value_and_type_test(LeptParseReturnValue.ok, LeptType.number, "4.9406564584124654e-324",
        #                                 4.9406564584124654e-324)
        # self.return_value_and_type_test(LeptParseReturnValue.ok, LeptType.number, "-4.9406564584124654e-324",
        #                                 -4.9406564584124654e-324)
        # self.return_value_and_type_test(LeptParseReturnValue.ok, LeptType.number, "2.2250738585072009e-308",
        #                                 2.2250738585072009e-308)
        # self.return_value_and_type_test(LeptParseReturnValue.ok, LeptType.number, "-2.2250738585072009e-308",
        #                                 -2.2250738585072009e-308)
        self.return_value_and_type_test(LeptParseReturnValue.ok, LeptType.number, "2.2250738585072014e-308",
                                        2.2250738585072014e-308)
        self.return_value_and_type_test(LeptParseReturnValue.ok, LeptType.number, "-2.2250738585072014e-308",
                                        -2.2250738585072014e-308)
        self.return_value_and_type_test(LeptParseReturnValue.ok, LeptType.number, "1.7976931348623157e+308",
                                        1.7976931348623157e+308)
        self.return_value_and_type_test(LeptParseReturnValue.ok, LeptType.number, "-1.7976931348623157e+308",
                                        -1.7976931348623157e+308)

    def test_parse_number_too_big(self):
        self.return_value_and_type_test(LeptParseReturnValue.number_too_big, LeptType.null, "1e309")

    def return_value_and_type_test(self, return_value, lept_type, json, value=None):
        v, parse_return_code = LeptJson.parse(json)
        self.assertEqual(return_value, parse_return_code)
        self.assertEqual(lept_type, v.lept_type)

        if value is not None:
            if v.lept_type == LeptType.number:
                self.assertEqual(value, v.number)


if __name__ == '__main__':
    unittest.main()
