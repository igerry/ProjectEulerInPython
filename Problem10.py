#!/usr/bin/python

class Problem10:
    '''
    Summation of primes
    Problem 10
    142913828922

    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
    '''

    def solution(self):
        summ = 0
        primes = []
        nextPrime = 0
        
        while nextPrime < 2000000:
            summ += nextPrime
            nextPrime = self.getNextPrime(primes)
            print(nextPrime)
        return summ

    def getNextPrime(self, primes):
        if (len(primes) == 0):
            primes.append(2)
            return 2

        if (len(primes) == 1):
            primes.append(3)
            return 3

        findNewPrime = False
        nextPrime = primes[-1] + 2
        while not findNewPrime:
            findNewPrime = True
            for i in primes:
                if not nextPrime % i:
                    findNewPrime = False
                    break
          
            if (findNewPrime):
                primes.append(nextPrime)
                break
            
            nextPrime += 2

        return nextPrime

p = Problem10()
print(p.solution())