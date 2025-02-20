# PROBLEM DESCRIPTION
# Given a set of 5 data points of Tesla stocks, we need to interpolate the data in a polynomial P_4(t) and
# consequently compute P_4(t=6) using the polynomial P_4(t) function.


# ALGORITHM DESCRIPTION
# The algorithm follows Lagrange's sinterpolation solution for polynomial interpolations. Since we are
# given five data points, we will create a P_4(t) polynomial by following his general case, where given
# n+1 points, we can create an n-th order polynomial.

tesla_stock = {
    1: 412,
    2: 407,
    3: 397,
    4: 398,
    5: 417
}

def polynomial(x):
    x1, x2, x3, x4, x5 = 1, 2, 3, 4, 5
    y1, y2, y3, y4, y5 = tesla_stock[1], tesla_stock[2], tesla_stock[3], tesla_stock[4], tesla_stock[5]
    term1 = y1*(((x-x2)*(x-x3)*(x-x4)*(x-x5))/((x1-x2)*(x1-x3)*(x1-x4)*(x1-x5)))
    term2 = y2*(((x-x1)*(x-x3)*(x-x4)*(x-x5))/((x2-x1)*(x2-x3)*(x2-x4)*(x2-x5)))
    term3 = y3*(((x-x1)*(x-x2)*(x-x4)*(x-x5))/((x3-x1)*(x3-x2)*(x3-x4)*(x3-x5)))
    term4 = y4*(((x-x1)*(x-x2)*(x-x3)*(x-x5))/((x4-x1)*(x4-x2)*(x4-x3)*(x4-x5)))
    term5 = y5*(((x-x1)*(x-x2)*(x-x3)*(x-x4))/((x5-x1)*(x5-x2)*(x5-x3)*(x5-x4)))

    return term1 + term2 + term3 + term4 + term5

print(polynomial(6))