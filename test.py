#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import unittest
from lept_constants import LeptType, LeptParseReturnValue
from leptjson import LeptValue, LeptJson

class LeptTest(unittest.TestCase):
    
    def test_parse_null(self):
        v, parse_return_code = LeptJson.Parse("null")
        self.assertEqual(LeptParseReturnValue.ok, parse_return_code)
        self.assertEqual(LeptType.null, v.type)
        
    def test_parse_expect_value(self):
        v, parse_return_code = LeptJson.Parse("")
        self.assertEqual(LeptParseReturnValue.expect_value, parse_return_code)
        self.assertEqual(LeptType.null, v.type)
        
        v, parse_return_code = LeptJson.Parse("  ")
        self.assertEqual(LeptParseReturnValue.expect_value, parse_return_code)
        self.assertEqual(LeptType.null, v.type)
        
    def test_parse_invalid_value(self):
        v, parse_return_code = LeptJson.Parse("nul")
        self.assertEqual(LeptParseReturnValue.invalid_value, parse_return_code)
        self.assertEqual(LeptType.null, v.type)
        
        v, parse_return_code = LeptJson.Parse("?")
        self.assertEqual(LeptParseReturnValue.invalid_value, parse_return_code)
        self.assertEqual(LeptType.null, v.type)
        
    def test_parse_root_not_singular(self):
        v, parse_return_code = LeptJson.Parse("null x")
        self.assertEqual(LeptParseReturnValue.root_not_singular, parse_return_code)
        self.assertEqual(LeptType.null, v.type)
            
if __name__ == '__main__':
    unittest.main()