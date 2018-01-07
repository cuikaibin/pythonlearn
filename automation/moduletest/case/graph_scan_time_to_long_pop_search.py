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
    def test_scan_time_to_long_pop_search(self): 
        """
        #需要执行的case
        """
        self.mp.enter_into_graph_search()
    
        general_icon=self.mp.driver.find_element_by_name("扫一扫").click()
        time.sleep(15)
        self.mp.driver.find_element_by_name("扫一扫")
        time.sleep(15)
        self.mp.driver.find_element_by_name("扫一扫")
        time.sleep(15)
        self.mp.driver.find_element_by_name("扫一扫")
        time.sleep(17)

        #wait timeout
        self.mp.driver.find_element_by_name("关闭").click()
        #self.driver.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]").click()
        time.sleep(3)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GraphFunctionTests)
    unittest.TextTestRunner(verbosity=2).run(suite) #执行case集
