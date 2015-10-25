#!/usr/bin/python

class NumberCombination(object):
    def __init__(self, number_list, number):
        self.number_list = number_list
        self.number_list_len = len(number_list)
        self.number = number
        self.result = []

    def process(self):
        # Sort number list
        self.number_list.sort()
        i = 0
        j = 0
        lst = []
        while i < self.number_list_len:
            lst_sum = sum(lst)
            lst_len = len(lst)

            if lst_sum < self.number:
                lst.append(self.number_list[i])
                i += 1
            else:
                if lst_sum == self.number:
                    self.result.append(list(lst))
                    if 1 == lst_len:
                        lst.pop()
                else:
                    if 1 == lst_len:
                        break
                if  lst_len > 1:
                    lst.pop()
                    lst.pop()
                    i -= 1

            lst_len = len(lst)

            if lst_len == 0:
                j += 1
                i = j


    def display(self):
        for i in xrange(len(self.result)):
            print ','.join(map(str,self.result[i]))

if '__main__' == __name__:
    nc = NumberCombination([2,4,6,7,3,8,1,5,9,13], 9)
    nc.process()
    nc.display()
