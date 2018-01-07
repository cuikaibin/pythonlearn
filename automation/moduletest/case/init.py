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
        跳过引导页
        """

        #获取屏幕长度
        x = self.mp.driver.get_window_size()['width']
        y = self.mp.driver.get_window_size()['height']
        self.mp.driver.swipe(x * 0.6, y * 0.3, x * 0.6, y * 0.2)
        time.sleep(2)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GraphFunctionTests)
    unittest.TextTestRunner(verbosity=2).run(suite) #执行case集
