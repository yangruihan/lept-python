#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from lept_constants import LeptType, LeptParseReturnValue

class LeptValue:
    def __init__(self, lept_type=None):
        if lept_type == None:
            self.type = LeptType.null
        else:
            self.type = lept_type
    
class LeptJson:
    
    lept_value = LeptValue()
    lept_context = ''
    
    @classmethod
    def Parse(self, json):
        LeptJson.lept_context = json
        LeptJson.ParseWhitespace()
        parse_return_code = LeptJson.ParseValue()
        if parse_return_code == LeptParseReturnValue.ok and len(LeptJson.lept_context.strip()) != 0:
            return LeptValue(LeptType.null), LeptParseReturnValue.root_not_singular
        else:
            return LeptJson.lept_value, parse_return_code

    @classmethod
    def ParseWhitespace(self):
        LeptJson.lept_context = LeptJson.lept_context.strip()

    @classmethod
    def ParseValue(self):
        if len(LeptJson.lept_context) == 0:
            LeptJson.lept_value.type = LeptType.null
            return LeptParseReturnValue.expect_value
        elif LeptJson.lept_context[0] == 'n':
            return LeptJson.ParseNull()
        elif LeptJson.lept_context[0] == 't':
            return LeptJson.ParseTrue()
        elif LeptJson.lept_context[0] == 'f':
            return LeptJson.ParseFalse()
        else:
            LeptJson.lept_value.type = LeptType.null
            return LeptParseReturnValue.invalid_value

    @classmethod
    def ParseNull(self):
        assert(LeptJson.lept_context[0] == 'n')
        if (LeptJson.lept_context[0:4] != 'null'):
            return LeptParseReturnValue.invalid_value
        LeptJson.lept_context = LeptJson.lept_context[4:]
        LeptJson.lept_value.type = LeptType.null
        return LeptParseReturnValue.ok
        
    @classmethod
    def ParseTrue(self):
        assert(LeptJson.lept_context[0] == 't')
        if (LeptJson.lept_context[0:4] != 'true'):
            return LeptParseReturnValue.invalid_value
        LeptJson.lept_context = LeptJson.lept_context[4:]
        LeptJson.lept_value.type = LeptType.true
        return LeptParseReturnValue.ok
        
    @classmethod
    def ParseFalse(self):
        assert(LeptJson.lept_context[0] == 'f')
        if (LeptJson.lept_context[0:5] != 'false'):
            return LeptParseReturnValue.invalid_value
        LeptJson.lept_context = LeptJson.lept_context[5:]
        LeptJson.lept_value.type = LeptType.false
        return LeptParseReturnValue.ok