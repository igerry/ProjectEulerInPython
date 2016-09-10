
class Problem1:
	"""
 	Multiples of 3 and 5
	Problem 1
 	233168
 
 	If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
 
 	Find the sum of all the multiples of 3 or 5 below 1000.
	"""

	def solution(self):
		all_sum = sum( number for number in xrange(1000) if not (number % 3 and number % 5) )
		return all_sum

problem = Problem1()
print problem.solution()