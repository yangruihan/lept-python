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
        
    def return_value_and_type_test(self, return_value, type, json):
        v, parse_return_code = LeptJson.Parse(json)
        self.assertEqual(return_value, parse_return_code)
        self.assertEqual(type, v.type)
            
if __name__ == '__main__':
    unittest.main()