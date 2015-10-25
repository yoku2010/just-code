#!/usr/bin/python

class BinaryMatrix(object):
    def __init__(self):
        self.matrix = [
            [1,0,1,1,0],
            [0,1,1,1,0],
            [1,1,1,1,1],
            [1,0,1,1,1],
            [1,1,1,1,1]
        ]
        self.temp_storage = 0   #Initial Declaration O(1) space complexity

    def process(self):
        self.temp_storage = self.matrix[0][0]           # Step - 1

        for i in xrange(1, len(self.matrix)):
            self.temp_storage &= self.matrix[0][i]      # Step - 2
            self.matrix[0][0] &= self.matrix[i][0]      # Step - 3

        for i in xrange(1, len(self.matrix)):
            for j in xrange(1, len(self.matrix)):
                self.matrix[0][i] &= self.matrix[j][i]  # Step - 4
                self.matrix[i][0] &= self.matrix[i][j]  # Step - 5

        for i in xrange(1, len(self.matrix)):
            for j in xrange(1, len(self.matrix)):
                self.matrix[i][j] = self.matrix[i][0] & self.matrix[0][j]   # Step - 6

        for i in xrange(1, len(self.matrix)):
            if 0 == self.matrix[0][0]:
                self.matrix[0][i] = 0                   # Step - 7
            if 0 == self.temp_storage:
                self.matrix[i][0] = 0                   # Step - 7

        self.matrix[0][0] = self.matrix[0][0] & self.temp_storage           # Step - 8


    def display(self):
        for i in xrange(len(self.matrix)):
            print ' '.join(map(str,self.matrix[i]))

if '__main__' == __name__:
    bm = BinaryMatrix()
    bm.process()
    bm.display()
