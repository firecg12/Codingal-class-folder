import math 
import random

print("The ceil value of 26.7 is:", str(math.ceil(26.7)))
print("The floor value of 45.9 is:", str(math.floor(45.9)))
# The ceil function returns the smallest integer greater than or equal to a given number.
# The floor function returns the largest integer less than or equal to a given number.

# using copysign function
x = +12
y = -15

print("The copysign value of x  from y is:", str(math.copysign(x, y)))

# using absolute values(fabs)

print("The absolute value of -78 is:", str(math.fabs(-78)))
print("The absolute value of 56 is:", str(math.fabs(56)))

# gcd function
print("The gcd value of 24,56 and 78 is:", str(math.gcd(24,56,78)))
# using
print("The random integer value between 4 - 9 is:", str(random.randint(4,9)))