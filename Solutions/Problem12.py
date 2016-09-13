#!/usr/bin/python

class Problem12:
    '''
    Problem 12: Highly divisible triangular number
    76576500

    The sequence of triangle numbers is generated by adding the natural numbers. 
    So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ... 

    Let us list the factors of the first seven triangle numbers:
    1:1 
    3:1,3 
    6:1,2,3,6
    10:1,2,5,10 
    15:1,3,5,15 
    21:1,3,7,21 
    28:1,2,4,7,14,28

    We can see that 28 is the first triangle number to have over five divisors.
    What is the value of the first triangle number to have over five hundred divisors?
    '''

    def solution(self):
        n = 0
        count = 0
        while count < 500:
            n =  n + 1
            if not n % 2:
                count = self.combine_divisors(n/2, n+1)
            else:
                count = self.combine_divisors((n+1)/2, n)
            print '(%d, %d)' % (n * (n+1) / 2, count)

        return n * (n+1) / 2

    def combine_divisors(self, a, b):
        return self.number_of_divisors(a) * self.number_of_divisors(b)

    def number_of_divisors(self, number):
        count = 0
        for i in range( int(number / 2) ):
            if not number % (i+1):
                count += 1
        return count + 1

p = Problem12()
print p.solution()