#!/usr/bin/python

"""
@author: Yogesh Kumar
@summary: To draw a spiral pattern of numbers like that.

Enter Number of Element: 21

17     	16     	15     	14     	13
18     	5      	4      	3      	12
19     	6      	1      	2      	11
20     	7      	8      	9      	10
21

"""


def spiral_pattern(number):
    n = 2

    while True:
        if number <= n*n:
            a = [["-" for x in range(n)] for y in range(n)]
            break
        n += 2

    k = 0
    l = n*n + 1

    c1 = 0
    c2 = n - 1

    r1 = 0
    r2 = n - 1

    while k<n*n:
        for i in range(c1, c2 + 1):
            k+=1
            a[r1][i] = l - k <= number and l - k or ""

        for i in range(r1 + 1, r2 + 1):
            k+=1
            a[i][c2] = l - k <= number and l - k or ""

        for i in range(c2-1, c1 - 1, -1):
            k+=1
            a[r2][i] = l - k <= number and l - k or ""

        for i in range(r2-1, r1, -1):
            k+=1
            a[i][c1] = l - k <= number and l - k or ""

        c1 += 1
        c2 -= 1
        r1 += 1
        r2 -= 1

    print_pattern(a, n);

def print_pattern (a, n):
    print "The Spiral Matrix is: "
    print "\n".join(map(str, ["\t".join(map(str,a[i])) for i in range(n)]))

if __name__ == "__main__":
    number = int(raw_input("Enter Number of Element: "));
    spiral_pattern(number);
