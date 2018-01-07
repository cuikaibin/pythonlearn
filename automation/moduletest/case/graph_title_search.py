#!/usr/bin/python
# encoding: utf-8
"""
Create on 2017-7-24
python 2.7 for mac
@author: cuikaibin
"""

import os
import time
from lib.base import Case
from lib.base import CaseConfig
from selenium import webdriver

#Appium环境配置
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class GraphFunctionTests(Case):
    """
    class
    """
    def test_scan_text_search1(self):
        """
        需要执行的case
        """
        self.mp.enter_into_graph_search()
        general_icon=self.mp.driver.find_element_by_name("题目").click()
        time.sleep(7)
        self.mp.from_graph_sdk_goto_pic_select()

        #题目垂类
        search_config = CaseConfig()
        search_file=search_config.get_picture_name("title_search")
        self.mp.driver.find_element_by_name(search_file).click()
        time.sleep(3)

        #发起搜索
        self.mp.driver.find_element_by_name("mis image editor search").click()
        time.sleep(5)
        
    def test_scan_text_search2(self):
        """
        返回手百首页
        """
        try:
            self.mp.driver.find_element_by_name("BBAUIKit.bundle/BBAToolBar/BBAToolBarSystemItemImage1001bgStyle1.png").click()
            print "click homepage button"
        except:
            print "We have been on the homepage"

        self.mp.enter_into_graph_search()
        
        general_icon=self.mp.driver.find_element_by_name("题目").click()
        time.sleep(7)
        self.mp.from_graph_sdk_goto_pic_select()

        #题目垂类
        search_config = CaseConfig()
        search_file=search_config.get_picture_name("title_search")
        self.mp.driver.find_element_by_name(search_file).click()
        time.sleep(3)

        #旋转90度
        self.mp.driver.find_element_by_name("mis image editor rotate normal").click()
        time.sleep(2)
        #重拍
        self.mp.driver.find_element_by_name("mis image editor remake").click()
        self.mp.from_graph_sdk_goto_pic_select()
        search_config = CaseConfig()
        search_file=search_config.get_picture_name("title_search")
        self.mp.driver.find_element_by_name(search_file).click()
        time.sleep(3)

        #发起搜索
        self.mp.driver.find_element_by_name("mis image editor search").click()
        time.sleep(5)
        self.mp.driver.find_element_by_name("框选").click()
        time.sleep(2)
        self.mp.driver.find_element_by_name("mis image editor search").click()
        time.sleep(5)
        self.mp.driver.find_element_by_name("重拍").click()

        time.sleep(5)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GraphFunctionTests)
    unittest.TextTestRunner(verbosity=2).run(suite) #执行case集