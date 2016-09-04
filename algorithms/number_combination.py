#!/usr/bin/python

class NumberCombination(object):
    def __init__(self, number_list, number):
        self.number_list = number_list
        self.number = number
        self.result = []

    def process(self):
        '''
        Algorithm process
        '''
        # Make It Unique
        self.number_list = list(set(self.number_list))
        # Number Count
        self.number_list_len = len(self.number_list)
        # Sort number list
        self.number_list.sort()
        i = 0
        last_index = 0
        lst = []
        while i < self.number_list_len:
            # figure out sum of current combination list
            lst_sum = sum(lst)

            # check the sum of combination list is less, equal or greater then the given number
            if lst_sum < self.number:
                lst.append(self.number_list[i]) # add more number in combination list
                i += 1
            else:
                if lst_sum == self.number:
                    self.result.append(list(lst))   # append combination list into result list

                lst_len = len(lst)
                if 1 == lst_len:
                    break       # because there is no more combination exist.
                elif lst_len > 1:
                    lst.pop()   # pop the combination list
                    last_index = self.number_list.index(lst.pop())   # pop the combination list and find the last index
                    i = last_index + 1

        # if the last value is equal to the given number then add that into result list. because that will skip as per the logic of algorithm.
        if self.number_list[self.number_list_len - 1] == self.number:
            self.result.append([self.number])

    def display(self):
        '''
        Display the result list
        '''
        for i in xrange(len(self.result)):
            print ','.join(map(str,self.result[i]))

if '__main__' == __name__:
    nc = NumberCombination([2,4,6,7,3,8,1,5,9], 9)
    nc.process()
    nc.display()
