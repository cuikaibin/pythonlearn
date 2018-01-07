#!/usr/bin/env python
# encoding: utf-8
"""
define xts base case
"""
from frame.lib.controllib.bigenv.bigenv_case import BigenvCase
from frame.lib.controllib.bigenv.bigenv_case import BigenvPlugin
from frame.lib.controllib.normal.normal_case import NormalCase
from frame.lib.controllib.normal.normal_case import NormalPlugin
from frame.lib.commonlib.xtslog import xtslog
from frame.lib.commonlib import asserts
from frame.lib.commonlib.portalloc import PortAlloc
from frame.lib.commonlib import asserts
import json
import time
from appium import webdriver
from graphLogCheck import GraphLogCheck


class Case(NormalCase):
    """
    Case define
    """
    def __new__(cls):
        """
        redefine new
        """
        obj = NormalCase.__new__(cls)
        obj.mp_cls = Plugin

        return obj

    def __init__(self):
        # TODO
        self.mp = self.mp_cls()

        # 动态生成case
        self.register_cases()

        #手百结果页图搜icon
        self.graph_icon="search text field image button"

    def default_verify(self, pair_list):
        """
        not implement function
        """
        pass

    def register_strategy_case(self, name, data):
        """
        not implement function
        """
        pass

    def register_cases(self):
        """
        由需要动态生成case的继承类实现
        """
        pass

    def register_common_case(self, name, func, *args):
        """
        case register
        """
        def f(self, args=args):
            """
            function easy to use
            """
            func(*args)
        f.__name__ = 'test_{}'.format(name)
        f.__doc__ = name

        setattr(self.__class__, f.__name__, f)

    def record_log(self, reason="", server="", detail="", repair=""):
        """
        XTS log will be report in email
        """
        xtslog.error("Error_Reason:" + reason)
        xtslog.error("Error_Server:" + server)
        xtslog.error("Error_Detail:" + detail)
        xtslog.error("Error_Repair:" + repair)


class Plugin(NormalPlugin):
    """
    define Plugin
    """
    def __init__(self):
        """
        redefine __init__
        """
        NormalPlugin.__init__(self)

        #self.config = Config()

    def benchmark_env(self):
        """
        no implement
        """
        pass

    def startup_env(self):
        """
        no implement
        """
        print "this is startup_env"
        desired_caps = {}
        desired_caps['automationName'] = 'XCUITest'
        desired_caps['platformName']='iOS'
        desired_caps['deviceName']='iPhone 5se'
        desired_caps['device'] ='iOS'
        desired_caps['bundleId'] ='com.baidu.mms.qa'
        desired_caps['version'] ='10.1'
        desired_caps['udid']='99212a27584ea8c547b1ebcbed7398230d43cecb'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        pass

    def stop_env(self):
        """
        no implement
        """
        print "this is stop_env"
        self.driver.quit() #case执行完退出
        pass

    def clean_error(self):
        """
        no implement
        """
        pass

    def common_check(self, acase):
        """
        no implement
        """
        pass

    def diagnose_error(self):
        """
        no implement
        """
        pass

    def bak_failed_env(self, relpath):
        """
        no implement
        """
        pass
    def enter_into_graph_search(self):
        """
        手百首页进入图搜插件
        """
        time.sleep(2)
        try:
            self.driver.find_element_by_name("search text field image button").click()
            print "click graph button"
        except:
            print "we got error click graph again"
            self.driver.find_element_by_name("search text field image button").click()
        time.sleep(2)

    def from_graph_sdk_goto_pic_select(self):
        """
        图搜插件的某个垂类点击相册进入系统相册的 个人收藏
        """
        self.driver.find_element_by_name("底部工具条 打开相册").click()
        time.sleep(2)
        self.driver.find_element_by_name("查看相册").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[3]/XCUIElementTypeButton[1]").click()
        time.sleep(2)

class CaseConfig(NormalPlugin):
    """
    git test case config
    """
    def __init__(self):
        """
        init conf for case
        """
        self.picture={
            "cocacola":"照片, 个人收藏, 横排, 5月17日 11:01",
            "dress":"照片, 个人收藏, 竖排, 5月17日 11:17",
            "face":"照片, 个人收藏, 横排, 5月17日 11:16",
            "folower":"照片, 个人收藏, 横排, 5月15日 15:32",
            "medicine":"照片, 个人收藏, 横排, 2016年10月27日 16:49",
            "package":"照片, 个人收藏, 横排, 2013年12月01日 10:26",
            "text":"照片, 个人收藏, 横排, 5月17日 11:18",
            "wine":"照片, 个人收藏, 竖排, 5月17日 11:01",
            "scan_text":"照片, 个人收藏, 横排, 5月17日 11:53",
            "scan_care":"照片, 个人收藏, 竖排, 7月05日 16:34",
            "scan_product":"照片, 个人收藏, 横排, 7月06日 15:46",
            "scan_url":"照片, 个人收藏, 横排, 7月06日 15:44",
            "scan_pay":"照片, 个人收藏, 横排, 7月06日 15:48",
            "scan_EMS":"照片, 个人收藏, 横排, 7月06日 12:50",
            "title_search":"照片, 个人收藏, 横排, 7月17日 19:51",
            "translate_search":"照片, 个人收藏, 横排, 7月26日 19:00",
        }
        self.pic_res = {
            "cocacola":['3','可口可乐','G086 G202 G200 G217'],
            "dress":['3','连衣裙','G200 G202 G213 G207_1 G217'],
            "face":['3','','G202 G207 G213'],
            "flower":['3','玫瑰花', 'G202 G200 G215'],
            "medicine":['3','莲花清瘟胶囊','G209 G202 G213'],
            "package":['3','mk杀手包','G202 G200'],
            "text":['2','','G200 G202 G213'],
            "wine":['3','红酒','G086 G202 G200 G213'],
            "scan_text":"",
            "scan_care":"",
            "scan_product":"",
            "scan_url":"",
            "scan_pay":"",
            "scan_EMS":"",
            "title_search":"",
            "translate_search":"",
        }

    def get_picture_name(self,pkey):
        """
        get self.picture value for test
        """
        return self.picture[pkey]

    def check_search_result(self,start_time,index):
        """
        check result
        """
        print "start verify" + index
        check = GraphLogCheck(start_time,int(time.time()),
                set(self.pic_res[index][0].split()),
                self.pic_res[index][1],
                set(self.pic_res[index][2].split()))
        return check.check()


