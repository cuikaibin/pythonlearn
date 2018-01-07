#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: mvpState.py
Anthor: cuikaibin
Date: 2017/06/15
"""
import urllib
import urllib2
import json
import time
import sys 
import logging

"""
通过case执行ID获取case的执行状况
"""
class getInformation(object):

    def __init__(self, myId, sceneHistoryId):
        self.myId = myId
        self.sceneHistoryId = sceneHistoryId
        self.tds = []

    """
    获取场景的执行状态
    """
    def getJson(self):
        caseUrl = "http://mvp.baidu.com/mvpmobile/api/scene/historyResult?sceneId=%s&sceneHistoryId=%s" % (self.myId, self.sceneHistoryId)
        #print caseUrl
        try:
            html = urllib2.urlopen(caseUrl)
            hjson = json.loads(html.read())
            #print hjson
            a = hjson['data']['scene_result']
            if a == '0':
                return hjson['data']['scene_result']
            else:
                return hjson['data']['taskIds']
        except Exception as e:
            print 'mvp: get case judgement error, taskId %s, because: %s' % (self.myId, e)
            logging.exception(e)
            return '0'

    """
    报告内容文件
    """
    def mergeTr(self, casedata):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        if casedata[2] == 1:
            print "Info: Success!"
            state = "Case: Success!"
        else:
            print "Warning: Failed!"
            state = "Warning: Failed!" 
        f = open("trs.txt", 'a')
        if "Failed" in state:
            message = '<tr><td>%s</td><td>%s</td><td style="color:Red">%s</td></tr>' % (casedata[0], casedata[1], state)
        else:
            message = '<tr><td>%s</td><td>%s</td><td style="color:LimeGreen">%s</td></tr>' % (casedata[0], casedata[1], state) 
        f.write(message)
        f.close()
        
    """
    获取case的执行结果
    """
    def runResult(self, caseId):
        count = 0
        result = "8"
        caseUrl = "http://mvp.baidu.com/mvpmobile/api/taskapi/%s" % (caseId)
        print caseUrl
        while (count < 5):
            count = count + 1
            if result == "8":
                try:
                    html = urllib2.urlopen(caseUrl)
                    hjson = json.loads(html.read())
                    result = hjson['data']['testList'][0]['judgement']
                    caseName = hjson['data']['testList'][0]['sceneName']
                    print result
                    casedata = [caseId, caseName, result]
                    print casedata
                    return casedata
                except Exception as e:
                    time.sleep(15)
                    result = "8"
                    if count == 5:
                        print 'gitStatesFailed 5 times'
                        casedata = ["读取数据失败", "读取数据失败", 0] 
                        logging.exception(e)  
                        return casedata 

    """
    返回结果给日志
    """
    def backResult(self):
        #time.sleep(200)
        count = 0
        while (count < 30):
            value = self.getJson()
            #print value
            count = count + 1
            if value == '0':
                time.sleep(50)
            else:
                break
        caseList = " "
        caseList = value
        casedata = self.runResult(caseList)
        return casedata   

    """
    返回场景结果
    """
    def getResult(self):
        #time.sleep(200)
        count = 0
        while (count < 30):
            value = self.getJson()
            print value
            count = count + 1
            if value == '0':
                time.sleep(50)
            else:
                break
        caseList = " "
        caseList = value
        if ',' in caseList:
            caseIds = caseList.split(',')
            for number in range(len(caseIds)):
                caseId = caseIds[number]
                casedata = self.runResult(caseId)
                self.mergeTr(casedata)
        else:
            casedata = self.runResult(caseList)
            self.mergeTr(casedata)

if __name__ == '__main__':
    logCase = ['154', '156', '157', '107', '158', '159', '160']
    sceneId = sys.argv[1]
    sceneHistoryId = sys.argv[2]
    b = getInformation(sceneId, sceneHistoryId) 
    if sceneId in logCase:
        b.backResult()
    else:  
        b.getResult()