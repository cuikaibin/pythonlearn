#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
这是一个收银系统
'''
class CashSuper:

    def GetMoney(shelf, money):
        pass


class CashNormal(CashSuper):

    def GetMoney(shelf, money):
        return money


class CashRebate(CashSuper):

    def __init__(self, discount):
        self.discount = discount

    def GetMoney(self, money):
        realyMoney = money * self.discount
        return realyMoney


class CashReturn(CashSuper):

    def __init__(self, conditionMonkey, subMoney):
        self.conditionMonkey = conditionMonkey
        self.subMoney = subMoney

    def GetMoney(self, money):
        if money >= self.conditionMonkey:
            realyMoney = money - self.subMoney
        else:
            realyMoney = money 
        return realyMoney


class CashContext:

    peration = {\
    1: CashNormal(),
    2: CashRebate(0.8),
    3: CashReturn(300,100)}

    def __init__(self, cashClass, money):
        self.cashClass = cashClass
        self.money = money

    def getResult(self):
        if self.cashClass in self.peration:
            ctype = self.peration[self.cashClass]
            return ctype.GetMoney(self.money)


if __name__ == '__main__':
    ctype = input("type:[1]for normal,[2]for 80% discount [3]for 300 -100: ")  
    money = input('money: ')
    realyMoney = CashContext(ctype, money)
    print realyMoney.getResult()

