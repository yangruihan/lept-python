#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import math
import re

from lept_constants import LeptType, LeptParseReturnValue


class LeptValue:
    _number = 0
    _lept_type = LeptType.null

    def __init__(self, lept_type=None):
        if lept_type is not None:
            self._lept_type = lept_type

    @property
    def lept_type(self):
        return self._lept_type

    @lept_type.setter
    def lept_type(self, lept_type):
        self._lept_type = lept_type

    @property
    def number(self):
        assert (self._lept_type is not None and self._lept_type == LeptType.number)
        return self._number

    @number.setter
    def number(self, n):
        assert (self._lept_type is not None and self._lept_type == LeptType.number)
        self._number = n


class LeptJson:
    lept_value = LeptValue()
    lept_context = ''

    @classmethod
    def parse(cls, json):
        LeptJson.lept_context = json
        LeptJson.parse_white_space()
        parse_return_code = LeptJson.parse_value()
        if parse_return_code == LeptParseReturnValue.ok and len(LeptJson.lept_context.strip()) != 0:
            return LeptValue(LeptType.null), LeptParseReturnValue.root_not_singular
        elif parse_return_code != LeptParseReturnValue.ok:
            return LeptValue(), parse_return_code
        else:
            return LeptJson.lept_value, parse_return_code

    @classmethod
    def parse_white_space(cls):
        LeptJson.lept_context = LeptJson.lept_context.strip()

    @classmethod
    def parse_value(cls):
        if len(LeptJson.lept_context) == 0:
            LeptJson.lept_value.type = LeptType.null
            return LeptParseReturnValue.expect_value
        elif LeptJson.lept_context[0] == 'n' or LeptJson.lept_context[0] == 't' or LeptJson.lept_context[0] == 'f':
            return LeptJson.parse_literal()
        else:
            return LeptJson.parse_number()

    @classmethod
    def parse_literal(cls):
        assert (LeptJson.lept_context[0] == 'n' or LeptJson.lept_context[0] == 't' or LeptJson.lept_context[0] == 'f')
        if LeptJson.lept_context[0:4] == 'null':
            LeptJson.lept_value.lept_type = LeptType.null
            jump_len = 4
        elif LeptJson.lept_context[0:4] == 'true':
            LeptJson.lept_value.lept_type = LeptType.true
            jump_len = 4
        elif LeptJson.lept_context[0:5] == 'false':
            LeptJson.lept_value.lept_type = LeptType.false
            jump_len = 5
        else:
            return LeptParseReturnValue.invalid_value
        LeptJson.lept_context = LeptJson.lept_context[jump_len:]
        return LeptParseReturnValue.ok

    @classmethod
    def parse_number(cls):
        pattern = re.compile(r"^-?(0|[1-9]\d*)(\.\d+)?([Ee][+-]?\d+)?$")

        if not pattern.match(LeptJson.lept_context):
            return LeptParseReturnValue.invalid_value

        try:
            # TODO(coderyrh9236@gmail.com): float() 在处理非常大的正数或负数时精度丢失，待修复
            number = float(LeptJson.lept_context)

            if math.isinf(number):
                return LeptParseReturnValue.number_too_big

            LeptJson.lept_context = LeptJson.lept_context[len(str(number)):]
            LeptJson.lept_value.lept_type = LeptType.number
            LeptJson.lept_value.number = number
            return LeptParseReturnValue.ok
        except ValueError:
            return LeptParseReturnValue.invalid_value
