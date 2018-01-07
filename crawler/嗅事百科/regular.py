#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re

pattern = re.compile(r'<div(.\d+)>')

f = pattern.findall('qwuieu<4>alkdjl<div 3>jsaj<div 23>l3l;;;a1')
for i in f:
	print i


