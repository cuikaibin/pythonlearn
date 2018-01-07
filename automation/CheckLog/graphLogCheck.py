#!/usr/bin/python
#coding=utf-8

"""
File: graph-MVP.py
Author: zengling01(zengling01@baidu.com)
Date: 2017/05/12 10:35:28
"""

import os
import sys
import json
import time
from mvpState import getInformation

class GraphLogCheck(object):
    """
    根据主要的log_type、key、card_id校验每个case是否正确执行
    """
    def __init__(self, start_time, end_time, case_id):
        self.conf = {
        "154": ['6', '', ''],
        "160": ['23', '', 'G211 G213'],
        "159": ['23', '', 'G211 G213'],
        "158": ['23', '', 'G030 G213 G200 G015'],
        "156": ['3', '', 'G103 G001'],
        "107": ['23', '', 'G001 G103'],
        "157": ['3', '', 'G001 G103']
        }
        self.start_time = start_time
        self.end_time = end_time
        self.case_id = case_id
        self.param = self.conf[case_id]
        self.exp_log_type = set(self.param[0])
        self.key = self.param[1]
        self.exp_card_id = set((self.param[2]).split())
        self.page_num = 1
        self.cuid = "497A720F899F14929B39BBD41F1683D2|415527020929668"
        self.api_url = "http://xbug.baidu.com/api/drsync/glogse/graph/graph_log_api/GraphLog/"
        self.tds = []

    def TimestampToDate(self, timestamp):
        """
        将时间戳转换为日期
        """
        timeArray = time.localtime(timestamp)
        date = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        return date

    def check(self):
        """
        校验过程
        """
        log_api = ('curl -XPOST "%s" -d '
            '\'{"basic_param":{"start_time":%s,"page_num":%d,"cuid":"%s","end_time":%s}}\''
             % (self.api_url, self.start_time, self.page_num, self.cuid, self.end_time))
        print log_api
        try:
            ret = os.popen(log_api)
            content = ret.read()
            dictTmp = json.loads(content)
            result = ""
            log_types = set()
            card_ids = set()
            if dictTmp["status"] != 0:
                result = "Info-Warn: 未检索到日志"
            else:
                body = ""
                for obj in dictTmp["result"]["additional_info"]:
                    if obj["svc"] == "graph_search.b2log":
                        data = json.loads(obj["body"])
                        log_type = str(data["log_type"])
                        log_types.add(log_type)
                        if log_type == '3':
                            body = obj["body"].encode("utf-8")
                            for obj_card in data["show_info"]["show_results"]:
                                card_ids.add(obj_card["card_id"].encode("utf-8"))
                print "log_type: ", log_types
                print "card_id: ", card_ids
                if log_types or card_ids or self.case_id == "154":
                    flag = self.exp_log_type.issubset(log_types)
                    if self.key != "":
                        self.flag = flag and self.key in body
                    if self.exp_card_id != "":
                        self.flag = flag and self.exp_card_id.issubset(card_ids)
                    if self.flag:
                        result = "Info: Success!"
                    else:
                        result = "Warning: Failed!"
                        f = open(self.case_id + ".json", 'w')
                        f.write(content)
                        f.close()
                else:
                    result = "Info-Warn: Log error"
                    f = open(self.case_id + ".json", 'w')
                    f.write(content)
                    f.close()
            if "Warning" in result:
                return 0
            else:
                return 1
        except Exception as e:
            print "Info-Warn: Find exception " + str(e)
            return -1

    def judgeState(self, mvpResult, logResult):
        """
        mvpResult:mvp执行结果
        logResult:日志校验结果
        """
        if mvpResult[2] == 1 or logResult == 1:
            caseResult = 1
            print "Success ! mvpResult={} logResult={}".format(mvpResult[2], logResult)
        else:
            caseResult = 0
            print "Failed ! mvpResult={} logResult={}".format(mvpResult[2], logResult)
        self.mergeTr(mvpResult[0], mvpResult[1], caseResult)
    
    def mergeTr(self, caseId, caseName, result):
        """
        生成报告内容
        """
        reload(sys)
        sys.setdefaultencoding('utf-8')
        if result == 1:
            state = "Case: Success!"
        else:
            state = "Warning: Failed!" 
        f = open("trs.txt", 'a')
        if "Failed" in state:
            message = '<tr><td>%s</td><td>%s</td><td style="color:Red">%s</td></tr>' % (caseId, caseName, state)
        else:
            message = '<tr><td>%s</td><td>%s</td><td style="color:LimeGreen">%s</td></tr>' % (caseId, caseName, state) 
        f.write(message)
        f.close()

if __name__ == '__main__':
    start_time = sys.argv[1]
    end_time = sys.argv[2]
    case_id = sys.argv[3]
    sceneHistoryId = sys.argv[4]
    logCheck = GraphLogCheck(start_time, end_time, case_id)
    logRes = logCheck.check()
    b = getInformation(case_id, sceneHistoryId)
    mvpRes = b.backResult()
    print mvpRes, logRes
    print logCheck.judgeState(mvpRes, logRes)
