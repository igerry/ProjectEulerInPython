#!/usr/bin/python

class Problem3:
    '''
    Largest prime factor
    Problem 3
    6857

    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143
    '''
        
    def solution(self):
    	n = 600851475143
    	primess = []

        maxPrime = 0
        nextPrime = 0

        while (n > 1):  
            nextPrime = self.getNextPrime(primess)
    
            while (not n % nextPrime):
                if (nextPrime > maxPrime):
                    maxPrime  = nextPrime
                n /= nextPrime
            print("%d, %d" % (maxPrime, n))

        return maxPrime

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

problem = Problem3()
print(problem.solution())