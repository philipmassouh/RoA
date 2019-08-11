# If n is a prime number, then for every a, 1 < a < n-1
# a^(n-1) % n = 1.

# If given a prime, it always returns true, otherwise it is
# probabalistic. (see Carmichael numbers). Accuracy can be increased
# by performing multiple iterations.

import math
import random

n = int(input("Enter a number for primality check: "))
k = int(input("Enter number of checks, greater means more accuracy: "))

b = True
i = 0

while (i<k) & (b):
	a = random.randint(2,n);
	if math.gcd(a, n) > 1 | pow(a, n-1) != 1:
		b = False
		print("Composite.")
	i += 1
if ~b:
	print("Probably prime.")	

		
		
		

