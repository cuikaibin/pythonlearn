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
    def test_scan_text_search(self):
        """
        需要执行的case
        """
        self.mp.enter_into_graph_search()
        general_icon=self.mp.driver.find_element_by_name("扫一扫").click()
        time.sleep(2)
        self.mp.from_graph_sdk_goto_pic_select()

        #网址二维码
        search_config = CaseConfig()
        search_file=search_config.get_picture_name("scan_url")
        self.mp.driver.find_element_by_name(search_file).click()
        time.sleep(3)

        #回到图搜
        self.mp.driver.find_element_by_name(self.graph_icon).click()


        time.sleep(5)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GraphFunctionTests)
    unittest.TextTestRunner(verbosity=2).run(suite) #执行case集