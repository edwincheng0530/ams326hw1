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

tesla_stock = {
    1: 412,
    2: 407,
    3: 397,
    4: 398,
    5: 417
}

def quadratic(x):
    A_list, B_list = [], []
    for key, value in tesla_stock.items():
        currRow = []
        B_list.append(value)
        for power in [0, 1, 2]:
            currRow.append((key**power))
        A_list.append(currRow)
    
    A_matrix = np.array(A_list)
    AT_matrix = A_matrix.T
    B_matrix = np.array(B_list)#.t

    ATxA = np.matmul(AT_matrix, A_matrix)
    ATxB = np.matmul(AT_matrix, B_matrix)

    coefficients = np.linalg.solve(ATxA, ATxB)

    res = 0
    for i, coeff in enumerate(coefficients):
        res += coeff * (x**i)

    return res

print(quadratic(6))