#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
这是一个穿衣系统
'''

class Person(object):
    def __init__(self, name):
        self.name = name

    def show(self):
        print '{}正在穿衣服'.format(self.name)

class Finery(Person):
    className = None

    def __init__(self):
        super(Finery, self).__init__('')
        pass

    def decorate(self, className):
        self.className = className

    def show(self):
        if self.className is not None:
            self.className.show()


class TShirts(Finery):
    def __init__(self):
        super(TShirts, self).__init__()
        pass

    def show(self):
        print 'dress TShirts'
        self.className.show()


class BigTrouser(Finery):
    def __init__(self):
        super(BigTrouser, self).__init__()
        pass

    def show(self):
        print 'dress BigTrouser'
        self.className.show()


def main():
    p = Person('xiaocai')
    bt = BigTrouser()
    ts = TShirts()
    bt.decorate(p)
    ts.decorate(bt)
    ts.show()
    print ts.__class__.mro()


if __name__ == "__main__":  
    main() 







