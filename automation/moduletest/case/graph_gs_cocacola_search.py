#!/usr/bin/python
# encoding: utf-8
"""
Create on 2017-5-15
python 2.7 for mac
@author: kangweiwei
"""
import os
from selenium import webdriver
import time
from lib.base import Case
from lib.base import CaseConfig

#Appium环境配置
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class GraphFunctionTests(Case):
    """
    GraphFunctionTests
    """
    def test_gs_graph_cocacola_search1(self):
        """
        #需要执行的case
        """
        self.mp.enter_into_graph_search()
    
        general_icon=self.mp.driver.find_element_by_name("通用").click()
        time.sleep(2)

        album_icon=self.mp.driver.find_element_by_name("底部工具条 打开相册")
        album_icon.click()
        time.sleep(2)

        look_album_icon=self.mp.driver.find_element_by_name("查看相册")
        look_album_icon.click()

        time.sleep(2)
        personal_save=self.mp.driver.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[3]/XCUIElementTypeButton[1]")
        personal_save.click()
        st = int(time.time())
        #coca cola
        search_config = CaseConfig()
        search_file=search_config.get_picture_name("cocacola")
        self.mp.driver.find_element_by_name(search_file).click()

        time.sleep(15)

        #assert (True == search_config.check_search_result(st, "cocacola"))
        log_check = search_config.check_search_result(st, "cocacola")
        if log_check == True:
            print "gs_graph_cocacola_search1 log check is ture"
        else:
            print "gs_graph_cocacola_search1 log check is false"

    def test_gs_graph_cocacola_search2(self):
        """
        返回手百首页
        """
        try:
            self.mp.driver.find_element_by_name("BBAUIKit.bundle/BBAToolBar/BBAToolBarSystemItemImage1001bgStyle1.png").click()
            print "click homepage button"
        except:
            print "We have been on the homepage"
        
        self.mp.enter_into_graph_search()
    
        general_icon=self.mp.driver.find_element_by_name("通用").click()
        time.sleep(2)

        album_icon=self.mp.driver.find_element_by_name("底部工具条 打开相册")
        album_icon.click()
        time.sleep(2)

        look_album_icon=self.mp.driver.find_element_by_name("查看相册")
        look_album_icon.click()

        time.sleep(2)
        personal_save=self.mp.driver.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[3]/XCUIElementTypeButton[1]")
        personal_save.click()
        st = int(time.time())
        #coca cola
        search_config = CaseConfig()
        search_file=search_config.get_picture_name("cocacola")
        self.mp.driver.find_element_by_name(search_file).click()

        time.sleep(15)
        self.mp.driver.find_element_by_name(self.graph_icon).click()

        time.sleep(5)
        #assert (True == search_config.check_search_result(st, "cocacola"))
        log_check = search_config.check_search_result(st, "cocacola")
        if log_check == True:
            print "gs_graph_cocacola_search2 log check is ture"
        else:
            print "gs_graph_cocacola_search2 log check is false"
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GraphFunctionTests)
    unittest.TextTestRunner(verbosity=2).run(suite) #执行case集
