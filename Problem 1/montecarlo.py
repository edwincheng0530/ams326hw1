# PROBLEM DESCRIPTION
#

# ALGORITHM DESCRIPTION
# 


import math
import random

root = 0.641583

def f(x):
    return math.e ** (-x**3) - x**4 - math.sin(x)

def montecarlo(min_value = 0.5, max_value = 0.75):
    seed_value = 42
    random.seed(seed_value)
    iteration = 1
    while True:
        x = random.uniform(min_value, max_value)
        x = round(x, 5)
        y = f(x)
        
        print(str(iteration) + ")\tx: " + str(x) + "\ty: " + str(y), end="\n\n")
        if abs(root-x) < (0.5*(10**(-4))) or y == 0:
            break

        iteration += 1
    return 

montecarlo()