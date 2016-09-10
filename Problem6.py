#!/usr/bin/python

class Problem6:
    '''
    Sum square difference
    Problem 6
    25164150

    The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)^2 = 55^2 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    '''

    def solution(self):
        summ = 0
        sumSquare = 0
        for i in range(1, 100):
            summ += i
            sumSquare += i * i
        
        diff = summ * summ - sumSquare
        return diff

problem = Problem6()
print(problem.solution())