#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import unittest
from lept_constants import LeptType, LeptParseReturnValue
from leptjson import LeptValue, LeptJson

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
        
    def return_value_and_type_test(self, return_value, type, json, value=None):
        v, parse_return_code = LeptJson.Parse(json)
        self.assertEqual(return_value, parse_return_code)
        self.assertEqual(type, v.lept_type)
        
        if value != None:
            if v.lept_type == LeptType.number:
                self.assertEqual(value, v.number)
            
if __name__ == '__main__':
    unittest.main()