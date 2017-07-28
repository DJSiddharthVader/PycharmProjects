
## @file reeds4_hw5.py
# @title Math 1MP3 Assg 5
# @author meeeeeeeeeeeeeeeee
# @brief example plz work
# @details finds the sum of each slice of the first dimension in a 3D array and
        # returns a new 1D array with the sums
        # :param a: 3D array
        # :return:1D array
import numpy as np

def array_slicemean(a):
    b = []
    for x in range(len(a)):
        b.append(np.sum(a[x, :, :]))
    return np.array(b)

def array_poly(a, x):
    """creates a polynomial, where each term in a row of the aray is a coefficient of the polynomial's
    variable. Each polynomial term has a different exponent."""
    vec = []
    for y in range(len(a)):
        co = a[y, :]
        exp = 0
        tot = 0
        for z in co:
            tot += z*x**exp
            exp += 1
        vec.append(tot)
    return np.array(vec)

def check_inverse(a, b, tol=1e-8):
    """Checks whether b is the matrix inverse of a, within a certain tolerance (tol) and returns a
    boolean value"""
    #found np.subtract function and np.greater function in the SciPy documentation (docs.scipy.org)
    #worked with James Hommersen on part of this function
    if len(a) != len(b):
        raise ValueError
    elif len(a) != len(a[:, ]):
        raise ValueError
    elif len(b) != len(b[:, ]):
        raise ValueError
    else:
        dot = np.dot(a,b)
        I = np.eye(len(a), len(a))
        Diff = np.abs(np.subtract(I, dot))
        #DiffTF = np.greater(tol, Diff)
        Diffmax = np.amax(Diff)
        #if np.any(DiffTF) is False:
        if Diffmax >= tol:
            return print(False)
        else:
            return print(True)

def maxrows(a,m):
    """returns every row in an array who's mean is greater than m"""
    b = []
    for x in range(len(a)):
        if a[x].mean() > m:
            b.append(a[x])
    return np.array(b)



