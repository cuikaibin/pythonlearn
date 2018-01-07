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
        general_icon=self.mp.driver.find_element_by_name("翻译").click()
        time.sleep(7)
        self.mp.from_graph_sdk_goto_pic_select()

        #翻译垂类
        search_config = CaseConfig()
        search_file=search_config.get_picture_name("translate_search")
        self.mp.driver.find_element_by_name(search_file).click()
        time.sleep(3)

        #获取屏幕长度
        x = self.mp.driver.get_window_size()['width']
        y = self.mp.driver.get_window_size()['height']
        #涂抹操作：（参数1:起始点横坐标；参数2：起始点纵坐标；参数3：角度；参数4：滑动距离）
        self.mp.driver.swipe(x * 0.2, y * 0.3, 0, y * 0.2)       
        time.sleep(5)

        #搜索
        self.mp.driver.find_element_by_name("icon ok normal zh").click()
        time.sleep(5)

        #重涂
        try:
            self.mp.driver.find_element_by_name("icon furbish normal").click()
        except:
            #翻译失败
            self.mp.driver.find_element_by_name("我知道了").click()
            time.sleep(2)
            self.mp.driver.find_element_by_name("icon furbish normal").click()
        time.sleep(2)
        #切换语种
        self.mp.driver.find_element_by_name("picker change").click()
        time.sleep(2)
        self.mp.driver.swipe(x * 0.6, y * 0.3, 0, y * 0.2)
        time.sleep(5)
        self.mp.driver.find_element_by_name("icon ok normal zh").click()
        time.sleep(5)

        #重拍
        try:
            self.mp.driver.find_element_by_name("icon retake normal").click()
        except:
            self.mp.driver.find_element_by_name("我知道了").click()
            time.sleep(2)
            self.mp.driver.find_element_by_name("icon retake normal").click()
        time.sleep(5)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GraphFunctionTests)
    unittest.TextTestRunner(verbosity=2).run(suite) #执行case集