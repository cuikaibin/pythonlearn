#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re

pattern = re.compile(r'\d+')

f = pattern.search('qwuieu4alkdjl3jsaj23l3l;;;a1')
print f.group()


