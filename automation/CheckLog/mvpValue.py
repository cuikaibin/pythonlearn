#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
通过场景ID执行场景并返回case执行ID
"""

import urllib
import urllib2
import json
import time
import sys 
import logging

class GetValue(object):
    """
    执行场景返回historyid
    """

    def __init__(self, sceneId):
        self.sceneId = sceneId

    def trigger(self):
        API_URL = "http://mvp.baidu.com/mvpmobile/api/scene/trigger"
        postdata=self.get_postdata()
        count = 0
        mvpHistoryId = '0'
        while (count < 5):
            count = count + 1
            if mvpHistoryId == '0':
                try: 
                    headers = {"Content-type": "application/json"}
                    req = urllib2.Request(API_URL, headers=headers, data=json.dumps(postdata))
                    response = urllib2.urlopen(req)
                    the_page = response.read()
                    response.close()
                    hjson = json.loads(the_page)
                    mvpHistoryId = hjson['data']['historyId']
                    if mvpHistoryId != "0":
                        print mvpHistoryId
                        break
                except Exception as e:
                    #print ('mvp: trigger task %s connect error, because: %s. Input=%s' 
                    #    % (self.sceneId, e, postdata))
                    #logging.exception(e)
                    mvpHistoryId = '0'
                    time.sleep(20)
                    if count == 5:
                        print 'gitValueFailed 5 times'
        #print 'gitValueFailed 5 times' 
        #return "0"
                
            
    def get_postdata(self):
        username='liuwanzhen'
        password='20170601141658001'
        data={'sceneId': self.sceneId, 'username': username, 'password': password}
        return data

if __name__ == '__main__':
    sceneId = sys.argv[1]
    a = GetValue(sceneId)
    a.trigger()  

