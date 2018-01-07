#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: graph-MVP.py
Author: zengling01(zengling01@baidu.com)
Date: 2017/8/24 10:35:28
"""

import sys 

def reportToHTML():
    """
    产出HTML格式的报告
    """
    a = open("trs.txt", "r")
    lis = a.readlines()
    alltrs = '\n'.join(lis)
    f = open("report.html", "a")
    message = """
    <table border='1' width='800px'>
        <tr><th>caseId</th><th>caseName</th><th>result</th><tr>
        %s
    </table>
    """ % (alltrs)
    f.write(message)
    f.close()

if __name__ == '__main__':
    reportToHTML()