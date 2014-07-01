#!/usr/bin/python

#
# Private: Python doesn't support private variables. But python supports a technique called name mangling.
# This feature turns every member name prefixed with at least two underscores and suffixed with at most one underscore
# into _<className><memberName>. 
#
# Note: Why are Python's 'private' methods not actually private?
# The name scrambling is used to ensure that subclasses don't accidentally override the private methods 
# and attributes of their superclasses. It's not designed to prevent deliberate access from outside.
#
# Source: http://broken.build/2011/07/21/private-protected-and-public-in-python/

class Cup:
    _color = None    # protected variable
    __content = None # private variable

    def __init__(self, color):
        self._color = color

    def fill(self, beverage):
        self.__content = beverage

    def empty(self):
        self.__content = None

    def get_cup(self):
        if self.__content:
            print 'We have %s cup with %s.' % (self._color, self.__content)
        else:
            print 'We have empty %s cup.' % (self._color)


cup = Cup("red")
#print cup.__content    # gives an error
print dir(cup)
cup.fill('Coffee')
print cup._Cup__content
cup.get_cup()