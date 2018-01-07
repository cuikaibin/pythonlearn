#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
这是一个计算器
'''
class Operation:

    def GetRestlt(self):
        pass  


class OperationAdd(Operation):

    def GetRestlt(self):
        return self.pusha + self.pushb


class OperationSub(Operation):

    def GetRestlt(self):
        return self.pusha - self.pushb


class OperationUndef(Operation):

    def GetRestlt(self):
        print 'not finad opetation'
        return 0


class OperationFaction:
    
    operation = {\
    '+': OperationAdd(),
    '-': OperationSub()}

    def CreatOperation(self, operator):
        #self.operator = operator
        if operator in self.operation:
            result = self.operation[operator]
        else:
            result = OperationUndef()
        return result


if __name__ == '__main__':
    operator = raw_input('operator: ') 
    pusha = input('pusha: ')
    pushb = input('pushb：')
    faction = OperationFaction()
    operation = faction.CreatOperation(operator)
    operation.pusha = pusha
    operation.pushb = pushb
    print operation.GetRestlt()

