#!/usr/bin/python

#
# Private Class: You can define a class as a private (can't import in other file).
# Use a single underscore prefix
#
# Note: This is the official Python convention for 'internal' symbols; "from module import *" does not import underscore-prefixed objects.

class _Private:
    def __init__(self):
        print 'Private class constructor called.'

    def get_name(self):
        print 'Private Class'


if '__main__' == __name__:
    p = _Private()
    p.get_name()