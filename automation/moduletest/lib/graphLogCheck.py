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

class GraphLogCheck(object):
    """
    根据log_type,key,card_id校验case是否正确执行
    """
    def __init__(self, start_time, end_time, log_type, key, card_id):
        self.start_time = start_time
        self.end_time = end_time
        self.exp_log_type = log_type
        self.key = key
        self.exp_card_id = card_id
        self.page_num = 1
        self.device = "iphone 5se"
        self.cuid = "AA6A24883718C965F62F615D60756C398BF1D5055FRAEBMJFDB"
        self.api_url = "http://xbug.baidu.com/api/drsync/glogse/graph/graph_log_api/GraphLog/"

    def check(self):
        """
        校验过程
        """
        log_api = ('curl -s -XPOST "%s" -d '
            '\'{"basic_param":{"start_time":%s,"page_num":%d,"cuid":"%s","end_time":%s}}\''
             % (self.api_url, self.start_time, self.page_num, self.cuid, self.end_time))
        print log_api
        try:
            ret = os.popen(log_api)
            content = ret.read()
            dictTmp = json.loads(content)
            if dictTmp["status"] != 0:
                print "Warning: 未检索到日志"
            else:
                log_types = set()
                card_ids = set()
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
                if len(log_types) > 0 and len(card_ids) > 0:
                    self.flag = self.exp_log_type.issubset(log_types)
                    if self.key != "":
                        self.flag = self.flag and self.key in body
                    if len(self.exp_card_id) > 0:
                        self.flag = self.flag and self.exp_card_id.issubset(card_ids)
                    if self.flag:
                        print "Info: Success!"
                        return True
                    else:
                        print "Warning: Failed!"
                        return False
                else:
                    return True
        except Exception as e:
            print "Warning: find Exception " + str(e)
            return True

if __name__ == '__main__':
    start_time = sys.argv[1]
    end_time = sys.argv[2]
    exp_log_type = set(sys.argv[3])
    key = sys.argv[4]
    exp_card_id = set((sys.argv[5]).split())
    check = GraphLogCheck(start_time, end_time, exp_log_type, key, exp_card_id)
    check.check()
