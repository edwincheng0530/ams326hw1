# PROBLEM DESCRIPTION
# Implement a bisection algorithm that finds the root of a given function f(x) = e(-x^3) - x^4 - sinx.
# The root x, should be satsify the inequality |x-r| < 0.5 x 10^-4, where r is the actual root, approximated
# to be r = 0.641583. In the program, we need to specify the number of steps/iterations as well as the value
# of x as well as f(x) at each iteration of the bisection method.  

# ALGORITHM DESCRIPTION
# For the bisection method, we are given that the bounds are -1 and 1 for a and b respectively, where a 
# represents the left x-bound and b represents the right x-bound. At each iteration, we will take the middle value
# between a and b (essentially the average of a and b), m, and observe the value of f(m). If the value at the midpoint
# f(m) is greater than 0, then we know that the root must be between the range of (m, b], otherwise we know that the root
# is in [a, m).

import math

root = 0.641583
error = 0.5*(10**(-4))

# Method that effectively represents f(x) - returns the value y given x
def f(x):
    return math.e ** (-x**3) - x**4 - math.sin(x)

# Given parameters of a = -1 and b = 1
def bisection(a = -1, b = 1):
    flop, iteration = 0, 1
    while True:
        # Obtain a new value of x in the middle of a and b
        x = (a+b)/2
        flop += 1
        # Calculate y-value of this new x-value
        y = f(x)
        flop += 2
        
        print(str(iteration) + ")\ta: " + str(a) + "\tb: " + str(b))
        print("\tx: " + str(x) + "\ty: " + str(y), end="\n\n")

        flop += 1
        # If new x-value OR Y is within range error (0.00005), we have found the root
        if abs(root-x) < error or abs(y) < error:
            print("Estimated # of Floating Point Operations: " + str(flop))
            break
        # If the y-value > 0, then the root is to the right of x, update left range 
        elif y > 0:
            a = x
        # If the y-value < 0, then the root is to the left of x, update right range
        elif y < 0:
            b = x

        iteration += 1

bisection()