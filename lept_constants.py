#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from enum import Enum

class LeptType(Enum):
    null = 1
    false = 2
    true = 3
    number = 4
    string = 5
    array = 6
    object = 7
    
class LeptParseReturnValue(Enum):
    ok = 0
    expect_value = 1
    invalid_value = 2
    root_not_singular = 3