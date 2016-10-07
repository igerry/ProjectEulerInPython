#!/usr/bin/python

class Problem15:
    '''
    Problem 15: Lattice paths
    1048576

    Starting in the top left corner of a 2 corner.
    2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right
    How many such routes are there through a 20
    '''

    def solution(self):
        number_routes = self.next_routes(20)
        return number_routes

    def next_routes(self, n):
        if n == 1:
            return 2
        return 2 * self.next_routes(n - 1)


p = Problem15()
print p.solution()