# PROBLEM DESCRIPTION
# Implement Secan'ts method of finding roots given the function f(x) = e(-x^3) - x^4 - sinx.
# The root x, should be satsify the inequality |x-r| < 0.5 x 10^-4, where r is the actual root, approximated
# to be r = 0.641583. In the program, we need to specify the number of steps/iterations as well as the value
# of x as well as f(x) at each iteration of the bisection method.  

# ALGORITHM DESCRIPTION
# 


import math

root = 0.641583


def f(x):
    return math.e ** (-x**3) - x**4 - math.sin(x)
