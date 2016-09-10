#!/usr/bin/python

class Problem4:
    '''
    Largest palindrome product
    Problem 4
    906609

    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    '''

    def solution(self):
        maxPalindromic = 0
        for i in range(900, 999, 1):
            for j in range(900, 999, 1):
                number = i * j
                if self.checkPalindromic(number) and (number > maxPalindromic):
                    print(number)
                    maxPalindromic = number
        
        return maxPalindromic

    def checkPalindromic(self, number):
        pString = str(number)
        count = len(pString)
        check = True
        for i in range(count/2):
            ri = count - 1 - i
            c = pString[i]
            rc = pString[ri]
            if not c == rc :
                check = False
                break
        return check

problem = Problem4()
print(problem.solution())