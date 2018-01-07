#!/usr/bin/env python
# -*- coding: utf-8 -*-


import urllib
import urllib2
import logging


class xsbk:

    def __init__(self, url, user_agent):
        self.url = url
        self.user_agent = user_agent

    def gitHtml(self, page):
        try:
            url = self.url.format(str(page))
            print url 
            headers = {'User-Agent': self.user_agent}
            request = urllib2.Request(url,headers=headers)
            response = urllib2.urlopen(request)
            print response.read()
        except urllib2.URLError, e:
            logging.exception(e)
            if hasattr(e, 'code'):
                print e.code,
            if hasattr(e, 'reason'):
                print e.reason


url = 'http://www.qiushibaike.com/hot/page/{}'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
xsbk = xsbk(url = url, user_agent = user_agent)
xsbk.gitHtml(1)



