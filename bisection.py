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

def f(x):
    return math.e ** (-x**3) - x**4 - math.sin(x)

def bisection(a = -1, b = 1):
    y = 0
    iteration = 1
    while True:
        x = (a+b)/2
        y = f(x)
        
        print(str(iteration) + ")\ta: " + str(a) + "\tb: " + str(b))
        print("\tx: " + str(x) + "\ty: " + str(y), end="\n\n")
        if abs(root-x) < (0.5*(10**(-4))) or y == 0:
            break
        elif y > 0:
            a = x
        elif y < 0:
            b = x

        iteration += 1

bisection()