#!/usr/bin/python

class Problem14:
    '''
    Problem 14: Longest Collatz sequence
    837799

    The following iterative sequence is defined for the set of positive integers: n   n/2 (n is even)
    n 3n+1(nisodd)
    Using the rule above and starting with 13, we generate the following sequence:
    13 40 20 10 5 16 8 4 2 1
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
    Which starting number, under one million, produces the longest chain? NOTE: Once the chain starts the terms are allowed to go above one million.
    '''

    def solution(self):
        max_chain = 1
        max_number = 1
        number = 1
        while(number < 1000000):
            chain = self.collatz_len(number)
            if chain > max_chain:
                max_chain = chain
                max_number = number
                print (max_number, max_chain)

            number += 1
        return max_number 

    def collatz_len(self, n):
        next_n = n
        chain = 1
        while(next_n > 1):
            next_n = self.next_convert(next_n)
            chain += 1
        return chain

    def next_convert(self, n):
        next_n = n
        if n % 2:
            next_n = 3 * n + 1
        else:
            next_n = int(n / 2)
        return next_n

p = Problem14()
print p.solution()