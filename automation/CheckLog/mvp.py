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
import commands
import time
import os
from graphLogCheck import GraphLogCheck

class mvpUse(object):
    """
    通过case执行ID获取case的执行状况
    """
    def __init__(self, sceneId):
        """
        just init
        """
        self.sceneId = sceneId
        self.username='v_cuikaibin'
        self.password='123456'

    def sceneTrigger(self):
        """
        通过场景id触发场景返回historyid
        """
        API_URL = "http://mvp.baidu.com/mvpmobile/api/scene/trigger"
        data = {\
            'sceneId': self.sceneId, 
            'username': self.username, 
            'password': self.password}
        count = 0
        mvpHistoryId = '0'
        while (count < 5):
            count = count + 1
            if mvpHistoryId == '0':
                try: 
                    headers = {"Content-type": "application/json"}
                    req = urllib2.Request(API_URL, headers=headers, data=json.dumps(data))
                    response = urllib2.urlopen(req)
                    the_page = response.read()
                    hjson = json.loads(the_page)
                    mvpHistoryId = hjson['data']['historyId']
                    if mvpHistoryId != "0":
                        print mvpHistoryId
                        return mvpHistoryId
                except Exception as e:
                    print ('mvp: trigger task %s connect error, because: %s' 
                        % (self.sceneId, e))
                    #logging.exception(e)
                    mvpHistoryId = '0'
                    time.sleep(20)
                    if count == 5:
                        print 'gitValueFailed 5 times'
                        return 'gitValueFailed 5 times'

    def getJson(self, sceneHistoryId):
        """
        获取场景的执行状态
        return 0    表示case正在执行
        return 非0   表示caseid，为string，如果有多个case，中间会用‘，‘隔开
        """
        caseUrl = "http://mvp.baidu.com/mvpmobile/api/scene/historyResult?sceneId={}&sceneHistoryId={}".format(self.sceneId, sceneHistoryId)
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
            print 'mvp: get case judgement error, taskId {}, because: {}'.format(self.sceneId, e)
            #logging.exception(e)
            return '0'

    def runResult(self, caseId):
        """
        通过getJson（）返回的caseid获取case执行智能判断结果
        casedata是list[case执行id，case名称，case执行结果]
        """
        count = 0
        result = "8"
        caseUrl = "http://mvp.baidu.com/mvpmobile/api/taskapi/{}".format(caseId)
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
                        casedata = [caseId, "读取结果失败", 0] 
                        #logging.exception(e)  
                        return casedata 


def mvpReport(casedata):
    """
    将runResult（）返回的casedata生成html report
    """
    reload(sys)
    sys.setdefaultencoding('utf-8')
    if False == os.path.exists("graph.html"):
        try:
            file = open("graph.html", "w")
            file.write("<table border='1' width='800px'>")
            file.write("<tr><th>caseId</th><th>caseName</th><th>result</th><tr>")
        except Exception as e:
            print e
        finally:
            file.close()
    try:
        url = "http://mvp.baidu.com/#/mobile/101/task/app/detail/{}".format(casedata[0])
        if casedata[2] == 1:
            print "Info: Success!"
            state = "Case: Success!"
        else:
            print "Warning: Failed!"
            state = "Warning: Failed!" 
        file = open("graph.html", "a")
        if "Failed" in state:
            message = "<tr><td>{}</td><td>{}</td><td><a style='color:Red' href='{}'>{}</a></td></tr>".format(casedata[0], casedata[1], url, state)
        else:
            message = "<tr><td>{}</td><td>{}</td><td><a style='color:LimeGreen' href='{}'>{}</a></td></tr>".format(casedata[0], casedata[1], url, state) 
        print message
        file.write(message)
    except Exception as e:
        print e
    finally:
        file.close()

 
def pushPicture(picture, iphone='T3Q6T16525003572'):
    """
    push picture and updata iphone dcim
    iphone 为默认参数      
    
    """
    delete_status = 1
    a = 0
    while a < 2 and delete_status != 0:  
        delete_command = 'adb_graph -s {} shell rm -rf /sdcard/Pictures/baidu/*'.format(iphone)
        (delete_status, output) = commands.getstatusoutput(delete_command)
        print 'delete_status = ', delete_status
        time.sleep(5)
        a = a + 1

    push_status = 1
    a = 0
    while a < 2 and push_status != 0:       
        #push_command = 'adb -s {} push /Users/baidu/mms-jenkins/workspace/mms-android-graph-search-function-test/mms_android_graph/CheckLog/data/{} /sdcard/Pictures/baidu/'.format(iphone, picture)
        push_command = 'adb_graph -s {} push ./data/{} /sdcard/Pictures/baidu/'.format(iphone, picture)     
        (push_status, output) = commands.getstatusoutput(push_command)
        print picture, 'push_status =', push_status 
        time.sleep(5)
        a = a + 1

    updata_status = 1
    a = 0
    while a < 2 and updata_status != 0:
        usdata_command = 'adb_graph -s {} shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/Pictures/baidu/{}'.format(iphone, picture)
        (updata_status, output) = commands.getstatusoutput(usdata_command)
        print picture, 'updata_status =', updata_status
        time.sleep(5)
        a = a + 1

    if push_status == 0 and updata_status == 0 and delete_status == 0:
        state = 0
        print state 
        return state 

        
def backResult(sceneId):
    """
    等待case执行完成，与日志结果进行对比
    """
    start_time = time.time()
    count = 0
    mvp = mvpUse(sceneId)
    sceneHistoryId = mvp.sceneTrigger()
    while (count < 10):
        value = mvp.getJson(sceneHistoryId)
        print value
        count = count + 1
        if value == '0':
            time.sleep(50)
        else:
            break
    end_time = time.time()
    log_result = GraphLogCheck(start_time, end_time, sceneId).check()
    print log_result
    caseList = " "
    caseList = value
    casedata = mvp.runResult(caseList)
    if log_result == 1 or casedata[2] == 1:
        casedata[2] = 1
    else:
        casedata[2] = 0
    mvpReport(casedata) 


def getResult(sceneId):
    """
    等待case执行完毕，返回case执行结果，并生成html
    """
    mvp = mvpUse(sceneId)
    count = 0
    sceneHistoryId = mvp.sceneTrigger()
    if sceneHistoryId == 'gitValueFailed 5 times':
        casedata = [sceneId, '触发失败', 2]
        print casedata
        mvpReport(casedata)
    else:
        while (count < 10):
            value = mvp.getJson(sceneHistoryId)
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
            for caseId in caseIds:
                casedata = mvp.runResult(caseId)
                mvpReport(casedata)
        else:
            casedata = mvp.runResult(caseList)
            mvpReport(casedata)


def prepareCase(sceneId):
    """
    初始化case执行
    """
    mvp = mvpUse(sceneId)
    count = 0
    sceneHistoryId = mvp.sceneTrigger()
    if sceneHistoryId == 'gitValueFailed 5 times':
        print 'case fail'
    else:
        while (count < 3):
            value = mvp.getJson(sceneHistoryId)
            print value
            count = count + 1
            if value == '0':
                time.sleep(50)
            else:
                break

if __name__ == '__main__':  
    '''
    logCase = ['154', '156', '157', '107', '158', '159', '160']
    caseids = ['156', '150']
    #pushPicture(picture)
    for caseid in caseids:
        print caseid
        if caseid in logCase:
            backResult(caseid)
        else: 
            getResult(caseid)
    '''
    #rmpicture_cammand = 'adb -s 91CEBPC2HHV9 shell rm -f /sdcard/Pictures/baidu/*'
    #(rm_status, output) = commands.getstatusoutput(rmpicture_cammand)
    #print 'rm_status = ', rm_status
    #caseids = ['394', '368', '369', '370', '371', '372', '373', '375', '376', '377', '378', '379', '380']
    #caseids = ['369', '380', '379', '377']
    prepar_caseids = ['394', '382', '381']
    not_picture_caseids = ['368', '369', '421', '422', '423']
    caseids_string = sys.argv[1]
    caseid_picture = {\
    '370': 'scan_smn.png',
    '371': 'scan_pay.png',
    '372': 'problem.jpg',
    '373': 'scan_url.png',
    '375': 'scan_text.png',
    '376': 'scan_product.png',
    '377': 'scan_care.png',
    '378': 'gm.jpg',
    '379': 'essay.jpg',
    '380': 'translate.jpg'}
    if ',' in caseids_string:
        caseids = caseids_string.split(',')
        for caseid in caseids:
            if caseid in not_picture_caseids:
                getResult(caseid)
            elif caseid in prepar_caseids:
                prepareCase(caseid)
            else:
                pushPicture(caseid_picture[caseid])
                getResult(caseid)
    else:
        if caseids_string in not_picture_caseids:
            getResult(caseids_string)
        elif caseids_string in prepar_caseids:
            prepareCase(caseids_string)
        else:
            pushPicture(caseid_picture[caseids_string])
            getResult(caseids_string)

