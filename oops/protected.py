#!/usr/bin/python

#
# Protected: Python doesn't support protected variable. It supported by convention only.
#            By prefixing the name of your member with a single underscore,
#            you're telling others "don't touch this, unless you're a subclass" 
#
# Source: http://broken.build/2011/07/21/private-protected-and-public-in-python/

class Cup:
    color = None
    _content = None # protected variable

    def fill(self, beverage):
        self._content = beverage

    def empty(self):
        self._content = None

    def get_cup(self):
        if self._content:
            print 'We have %s cup with %s.' % (self.color, self._content)
        else:
            print 'We have empty %s cup.' % (self.color)

cup = Cup()
cup.color = "Green"
cup._content = "tea"
print dir(cup)
cup.get_cup()