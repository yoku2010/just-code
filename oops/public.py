#!/usr/bin/python

#
# Public: All member variables and methods are public by default in Python
#
# Source: http://broken.build/2011/07/21/private-protected-and-public-in-python/

class Cup:
    color = None
    content = None

    def fill(self, beverage):
        self.content = beverage

    def empty(self):
        self.content = None

    def get_cup(self):
        if self.content:
            print 'We have %s cup with %s.' % (self.color, self.content)
        else:
            print 'We have empty %s cup.' % (self.color)


cup = Cup()
cup.color = 'Blue'
cup.content = 'Tea'
cup.get_cup()
cup.empty()
cup.get_cup()
cup.fill('Coffee')
cup.get_cup()

