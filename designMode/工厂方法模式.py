#!/usr/bin/env python
# -*- coding: utf-8 -*-


class LeiFeng:
    def __init__(self, name):
        self.name = name 

    def Sweep(self):
        print self.name, '扫地'

    def Wash(self):
        print self.name, '洗衣'

    def BueRice(self):
        print self.name, '买米'


class Undergraduta(LeiFeng):
    def __init__(self, name):
        LeiFeng.__init__(self, name)


class Volunteer(LeiFeng):
    def __init__(self, name):
        LeiFeng.__init__(self, name)


class IFactory:
    def CreatLeiFeng(self):
        pass


class UndergradutaFactory(IFactory):
    def CreatLeiFeng(self):
        undergraduta = Undergraduta('undergraduta')
        return undergraduta


class VolunteerFactory(IFactory):
    def CreatLeiFeng(self):
        volunteer = Volunteer('volunteer')
        return volunteer    


def main():
    undergraduta = UndergradutaFactory()
    undergraduta.CreatLeiFeng().Sweep()
    volunteer = VolunteerFactory()
    volunteer.CreatLeiFeng().Wash()


if __name__ == "__main__": 
    main()
