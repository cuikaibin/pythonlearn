#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
代送礼物
'''

class GiveGift(object):
    def GiveDolls(self):
        pass

    def GiveFlowers(self):
        pass

    def GiveChocolate(self):
        pass


class Pursui(GiveGift):
    '''
    继承者类
    '''
    def __init__(self, girl):
        self.girl = girl 

    def GiveDolls(self):
        print self.girl, '送你洋娃娃'

    def GiveFlowers(self):
        print self.girl, '送你花'

    def GiveChocolate(self):
        print self.girl, '送你巧克力'


class Proxy(GiveGift):
    '''
    代理类
    '''
    '''
    def __new__(cls, girl):
        obj = GiveGift.__new__(cls)
        obj.ps = Pursui
        return obj
    '''

    def __init__(self, girl):
        self.girl = girl
        self.pursui = Pursui(self.girl)

    def GiveDolls(self):
        self.pursui.GiveDolls()
        self.pursui.GiveFlowers()
        self.pursui.GiveChocolate()

    '''
    def GiveFlowers(self):
        self.pursui.GiveFlowers()

    def GiveChocolate(self):
        self.pursui.GiveChocolate()
    '''

def main():
    proxy = Proxy('花花')
    proxy.GiveDolls()
    #proxy.GiveFlowers()
    #proxy.GiveChocolate()


if __name__ == "__main__":  
    main() 

