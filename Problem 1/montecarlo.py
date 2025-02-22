# PROBLEM DESCRIPTION
# Implement a version of the Monte Carlo method in order to obtain the root of the function
# f(x) = e(-x^3) - x^4 - sinx. We are given the range in which to perform the Monte Carlo
# method, in which the minimum value is 0.50 and the maximum value is 0.75 

# ALGORITHM DESCRIPTION
# For Monte Carlo's method, we randomly choose a point x between the range given to us,
# in which the minmium value is 0.50 and the maximum value is 0.75. We do this random
# guessing until the value x is close enough to the root (in which the value of f(x) given
# x is equal to 0)

import math
import random

root = 0.641583
error = 0.5*(10**(-4))

# Method that effectively represents f(x) - returns the value y given x
def f(x):
    return math.e ** (-x**3) - x**4 - math.sin(x)

def montecarlo(min_value = 0.50, max_value = 0.75):
    # Provide a seed value such that the random values are consistent throughout different runs
    seed_value = 42
    random.seed(seed_value)
    flop, iteration = 0, 1
    while True:
        # Obtain a random float between the range and round it to 5 decimal places
        x = random.uniform(min_value, max_value)
        x = round(x, 5)
        # Calculate y-value of this new x-value
        y = f(x)
        flop += 3
        
        print(str(iteration) + ")\tx: " + str(x) + "\ty: " + str(y), end="\n\n")
        
        flop += 1
        # If new x-value OR Y is within range error (0.00005), we have found the root
        if abs(root-x) < error or abs(y) < error:
            print("Estimated # of Floating Point Operations: " + str(flop))
            break

        iteration += 1
    return 

montecarlo()