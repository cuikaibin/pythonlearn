#!/usr/bin/python
# encoding: utf-8
"""
Create on 2017-5-15
python 2.7 for mac
@author: kangweiwei
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
    GraphFunctionTests
    """
    def test_gs_graph_medicine_search(self): 
        """ 
        #需要执行的case
        """
        self.mp.enter_into_graph_search()
        
        self.mp.driver.find_element_by_name("通用").click()             
        time.sleep(2)
        
        self.mp.from_graph_sdk_goto_pic_select()

        st = int(time.time())
        search_config = CaseConfig()
        search_file=search_config.get_picture_name("medicine")
        self.mp.driver.find_element_by_name(search_file).click()
        time.sleep(5)

        self.mp.driver.find_element_by_name(self.graph_icon).click()

        time.sleep(5)
        #assert (True == search_config.check_search_result(st,"medicine"))
        log_check = search_config.check_search_result(st, "medicine")
        if log_check == True:
            print "gs_graph_medicine_search log check is ture"
        else:
            print "gs_graph_medicine_search log check is false"

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GraphFunctionTests)
    unittest.TextTestRunner(verbosity=2).run(suite) #执行case集
