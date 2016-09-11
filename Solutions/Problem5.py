#!/usr/bin/python

class Problem5:
    '''
    Smallest Multiple
    Problem 5
    232792560

    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    '''

    def solution(self):
        divisors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        return self.lcm(divisors)

    def lcm(self, divisors):
        if len(divisors) == 0:
            return 0
        elif len(divisors) == 1:
            return divisors[0]
        elif len(divisors) == 2:
            return self.lcm2(divisors[0], divisors[1])
        else:
            condensed = divisors
            first = condensed[0]
            second = condensed[1]
            condensed = condensed[2:]
            condensed.append(self.lcm([first, second]))
            return self.lcm(condensed)

    def lcm2(self, first, second):
        bigger = max(first, second)
        current = bigger
        while (current % first) or (current % second):
            current += bigger
        print('lcm(%d, %d) -> %d' % (first, second, current))
        return current

problem = Problem5()
print(problem.solution())

 