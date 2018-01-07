#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Person(object):  
    def __init__(self, name):  
        self.name = name  
  
    def show(self):  
        print "dressed %s" % self.name  
  
  
class Finery(Person):  
    component = None  
  
    def __init__(self):  
        super(Finery, self).__init__("")  
        pass  
  
    def decorate(self, ct):  
        self.component = ct  
  
    def show(self):  
        if self.component is not None:  
            self.component.show()  
  
  
class TShirts(Finery):  
    def __init__(self):  
        super(TShirts, self).__init__()  
        pass  
  
    def show(self):  
        print "Big T-shirt "  
        self.component.show()  
  
  
class BigTrouser(Finery):  
    def __init__(self):  
        super(BigTrouser, self).__init__()  
        pass  
  
    def show(self):  
        print "Big Trouser "  
        self.component.show()  
  
  
def main():  
    p = Person("somebody")  
    bt = BigTrouser()  
    ts = TShirts()  
    bt.decorate(p)  
    ts.decorate(bt)  
    ts.show()  
    print ts.__class__.__mro__
  
if __name__ == "__main__":  
    main() 
