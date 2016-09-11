#!/usr/bin/python

class Problem9:
    '''
    Special Pythagorean triplet
    Problem 9
    31875000

    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    '''

    def solution(self):
        maxx = 1000
        summ = 0
        for i in range(1, int(maxx / 3)):
            for j in range(1, int((maxx - 1 - i) / 2)): 
                k = maxx - i - j
                if (i*i + j*j == k*k):
                    summ = i * j * k
                    
        return summ


p = Problem9()
print(p.solution())