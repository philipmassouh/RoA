# Pseudocode

# Input: an integer n > 1

# Let A be an array of Boolean values, indexed by integers 2 to n, initially
# all set to true

# for i = 2, 3, 4, ... , not exceeding sqrt(n):
    # if A[i] is true:
        # for j = i^2, i^2+i, i^2+2i, i^2+3i, ... , not exceeding n:
            # A[j] := false.

# Output: all i such that A[i] is true.
import math

print('Given integer input n, this script will print every prime number in [2, n]')

n = int(input("Enter n: "))
A = [True for i in range(1, n+1)]

for i in range(2, int(math.ceil(n**0.5))):
    if (A[i] == True):
        for j in range (i**2, n, i):
                A[j] = False

for k in range(2, n):
    if (A[k] == True):
        print(k)
