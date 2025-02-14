# PROBLEM DESCRIPTION
# Implement Newton's method of finding roots given the function f(x) = e(-x^3) - x^4 - sinx.
# The root x, should be satsify the inequality |x-r| < 0.5 x 10^-4, where r is the actual root, approximated
# to be r = 0.641583. In the program, we need to specify the number of steps/iterations as well as the value
# of x as well as f(x) at each iteration of the bisection method.  

# ALGORITHM DESCRIPTION
# For Newton's method, we are given that the initail root x0 is equal to 0. This initial root allows us to 
# create the next root values, x_1, x_2, and so on. Using the formula x_(i+1) = x_i - f(x_i) / f'(x_i), in which
# we use the current value of x_i along with the original function f(x) and the derivative of f(x). Because
# we are already given the function f(x) beforehand, we also know the derivative of f(x) beforehand, allowing us to
# update x_i at every iteration, until f(x_i) reaches 0.

import math

root = 0.641583

def f(x):
    return math.e ** (-x**3) - x**4 - math.sin(x)

def fprime(x):
    return math.e ** (-x**3)*-3*(x**2) - 4*(x**3) - math.cos(x)

def newton(x_0 = 0):
    x = x_0
    iteration = 1
    while True:
        y = f(x)
        yprime = fprime(x)
        
        print(str(iteration) + ")\tx: " + str(x) + "\ty: " + str(y), end="\n\n")

        if abs(root-x) < (0.5*(10**(-4))) or y == 0:
            break
        
        x = x-(y/yprime)   
        iteration += 1     

newton()