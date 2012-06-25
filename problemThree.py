# Project Euhler Problem Three
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# http://projecteuler.net/problem=3

def my_isprime(number):
	for i in range(number -1, 2, -1):
		if (number % i == 0):
			return False

	return True

import math
composite = 600851475143
#composite = 13195
factors = []
largestPrime = 2;

# use the range from 2 to square root of n and find the largest prime in that 
# range.
comp_sqr_root = int(math.sqrt(composite)) + 1;

for i in range(comp_sqr_root, 2, -1):
	rem = composite % i
	if (rem == 0):
		factors.append(i)
		#largestPrime = i
		#break

for f in factors:
	if (my_isprime(f) and f > largestPrime):
		largestPrime = f


print 'Largest Prime is: ' + str(largestPrime)


