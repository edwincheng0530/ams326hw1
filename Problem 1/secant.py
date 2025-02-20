# PROBLEM DESCRIPTION
# Implement Secant's method of finding roots given the function f(x) = e(-x^3) - x^4 - sinx.
# The root x, should be satsify the inequality |x-r| < 0.5 x 10^-4, where r is the actual root, approximated
# to be r = 0.641583. In the program, we need to specify the number of steps/iterations as well as the value
# of x as well as f(x) at each iteration of the bisection method.  

# ALGORITHM DESCRIPTION
# For the Secant method of finding roots, we are given two inital values, x_0 and x_1, which are equal to -1 
# and 1 respectively. For every iteration, we need the previous two values, in this case, x_0 and x_1, calculating
# The value of x+1 using the formula x_(i+1) = x_i - (x_i - x_(i-1)) *  f(x_i) / (f(x_i) - f(x_(i-1))). Thus, for
# each iteration, we calculate the value of x_(i+1), checking whether x_(i+1) is the root of the function f(x). 
# The values of x_i_minus_1 and x_i get updated properly in each iteration to represent x_i and x_(i+1) respectively
# in order to calculate the next x-value.

import math

root = 0.641583


def f(x):
    return math.e ** (-x**3) - x**4 - math.sin(x)

def secant(x_0 = -1, x_1 = 1):
    x_iminus_1, x_i = x_0, x_1

    print("0)\tx0: " + str(x_iminus_1) + "\tx1: " + str(x_i), end="\n\n")
    iteration = 1
    while True:
        y = f(x_i)
        y_iminus_1 = f(x_iminus_1)

        x_iplus_one = x_i - (x_i - x_iminus_1)*(y/(y-y_iminus_1))
        y_iplus_one = f(x_iplus_one)
        print(str(iteration) + ")\tx: " + str(x_iplus_one) + "\ty: " + str(y_iplus_one), end="\n\n")
        if abs(root-x_iplus_one) < (0.5*(10**(-4))) or y_iplus_one == 0:
            break

        x_iminus_1, x_i = x_i, x_iplus_one
        iteration += 1
    return 

secant()