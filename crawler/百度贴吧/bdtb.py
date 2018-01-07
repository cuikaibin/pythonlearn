# -*- coding: utf-8 -*-

import urllib
import urllib2
import re


#处理页面标签类
class Tool:
    #去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换为\t
    replaceTD= re.compile('<td>')
    #把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n    ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        #strip()将前后多余内容删除
        return x.strip()

#百度贴吧爬虫类
class BDTB:

    #初始化，传入基地址，是否只看楼主的参数
    def __init__(self,baseUrl,seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz='+str(seeLZ)
        self.tool = Tool()

    #传入页码，获取该页帖子的代码
    def getPage(self,pageNum):
        try:
            url = self.baseURL+ self.seeLZ + '&pn=' + str(pageNum)
            print url
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            #print response.read().decode('utf-8')
            return response.read().decode('utf-8')
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接百度贴吧失败,错误原因",e.reason
                return None

    #获取贴吧标题
    def gitTitle(self):
        page = self.getPage(1)
        htmlstring = page.encode("utf-8") 
        #print utf8string
        #print type(utf8string)
        pattern = re.compile(r'<title>【.*?】(.*?)【.*?】.*?</title>', re.S)
        pattern2 = re.compile(r'<title>【图片】纯原创我心中的NBA2014-2015赛季现役50大【nba吧】_百度贴吧</title>', re.S)
        pattern1 = re.compile(r'百度贴吧', re.S)
        result = re.findall(pattern, htmlstring)
        for i in result:
            print i

        '''
        if result:
            #print result.group()
            print result.group().strip()
        else:
            return None
        '''
    #
    def gitContent(self, page):
        htmlstring = page.encode("utf-8") 
        pattern1 = re.compile(r'<div id=(.*?)class=(.*?)>(.*?)</div>', re.S)
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items = re.findall(pattern, htmlstring)
        #print items
        #print '...................'
        for item in items:
            print '...........................'
            print self.tool.replace(item)
            

baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL,1)
page = bdtb.getPage(1)
bdtb.gitTitle()
bdtb.gitContent(page)

