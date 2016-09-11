#!/usr/bin/python

class Problem7:
    '''
    10001st prime
    Problem 7
    104743

    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10 001st prime number?
    '''

    def solution(self):
        primes = []
        nextPrime = 2
        for i in range(10001):
            print('%d, %d' % (i, nextPrime))
            nextPrime = self.getNextPrime(primes)
        return nextPrime

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

p = Problem7()
print(p.solution())