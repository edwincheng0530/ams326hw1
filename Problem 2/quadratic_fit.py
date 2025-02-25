import numpy as np

# PROBLEM DESCRIPTION
# Given a set of 5 data points of Tesla stocks, we need to create a function quadratic f(x) that will
# best fit the five points. Once we have this quadratic equation, we will need to approximate the 
# value of the Tesla stock on the 6th day, or x=6  


# ALGORITHM DESCRIPTION
# The algorithm follows a linear algebra method of finding the quadratic line of best fit.
# I implemented the normal equation for least squares such that given Ax = b, I solved for
# A^T * Ax = A^T *b, where A^t is the matrix A transposed. I first start by creating a matrix
# A of all the leading coefficients for the five data points that we have using the formula
# c_1 + c_2*t + c_3*t^2, where t represents the time in day of the Tesla stock data set.
# The matrix b is simply the price of the Tesla stocks on its given day. Thus, we are then
# able to solve for the values c_1, c_2, and c_3 for the quadratic line of best fit.

# PERFORMANCE
# The creation of a quadratic fit for the five days of Tesla stocks is also quite trivial like
# the Lagrange interpolation of this same set of data. We can easily solve the equation Ax = b,
# in which both A and b represent matrices of the leading coefficients of the data sets mapped
# onto c_1 + c_2*t + c_3*t^2 = y. The computation for this is trivial, and thus the time complexity
# for this algorithm can also be represented as O(1).

# Tesla stock data points | key = day, value = price  
tesla_stock = {
    1: 412,
    2: 407,
    3: 397,
    4: 398,
    5: 417
}

def quadratic(x):
    flop = 0
    A_list, B_list = [], []
    # For each data point (day, price), create A matrix and B matrix such that
    # A_list contains a list of coefficients of equation c_1 + c_2*t + c_3*t^2 for each day
    # and B_list contains the y value (price) of each x-value (day)
    for key, value in tesla_stock.items():
        currRow = []
        B_list.append(value)
        for power in [0, 1, 2]:
            currRow.append((key**power))
        A_list.append(currRow)
    
    # Create A matrix, B matrix and transposed A matrix
    A_matrix = np.array(A_list)
    AT_matrix = A_matrix.T
    B_matrix = np.array(B_list)#.t

    # Multiply to obtain product of AT*A matrix and AT*B matrix
    ATxA = np.matmul(AT_matrix, A_matrix)
    ATxB = np.matmul(AT_matrix, B_matrix)
    
    # Solve for x values in the equation Ax = B, where A and B are matrices
    coefficients = np.linalg.solve(ATxA, ATxB)
    flop += 6

    # Approximate value for x given the quadratic line of best fit
    res = 0
    for i, coeff in enumerate(coefficients):
        res += coeff * (x**i)
        flop += 2

    return res, flop

res, flop = quadratic(6)
print("Estimated # of Floating Point Operations: " + str(flop))
print("Q_2(t=6) = " + str(res))