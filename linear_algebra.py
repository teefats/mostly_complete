"""
This file contains a set of functions to practice your
linear algebra skills.

It needs to be completed using "vanilla" Python, without
help from any library.
"""


def gradient(w1, w2, x):
    """
    Given the following function f(x) = w1 * x1^2 + w2 * x2
    where x is a valid vector with coordinates [x1, x2]
    evaluate the gradient of the function at the point x

    :param w1: first coefficient
    :param w2: second coefficient
    :param x: a point represented by a valid tuple (x1, x2)
    :return: the two coordinates of gradient of f
    at point x
    :rtype: float, float
    """

    def gradient(w1, w2, x):
        x1, x2 = x
        gradx1=2*w1*x1 + w2 * x2
        gradx2= w2 + w1 * x1 ** 2
        return (gradx1, gradx2)
    raise NotImplementedError


def metrics(u, v):
    """
    Given two vectors u and v, compute the following distances/norm between
    the two and return them.
    - l1 Distance (norm)
    - l2 Distance (norm)

    If the two vectors have different dimensions,
    you should raise a ValueError

    :param u: first vector (list)
    :param v: second vector (list)
    :return: l1 distance, l2 distance
    :rtype: float, float
    :raise ValueError:
    """
    raise NotImplementedError


def list_mul(u, v):
    """
    Given two vectors, calculate and return the following quantities:
    - element-wise sum
    - element-wise product
    - dot product

    If the two vectors have different dimensions,
    you should raise a ValueError

    :param u: first vector (list)
    :param v: second vector (list)
    :return: the three quantities above
    :rtype: list, list, float
    :raise ValueError:
    """
    raise NotImplementedError


def matrix_mul(A, B):
    """
    Given two valid matrices A and B represented as a list of lists,
    implement a function to multiply them together (A * B). Your solution
    can either be a pure mathematical one or a more pythonic one where you
    make use of list comprehensions.

    For example:
    A = [[1, 2, 3],
         [4, 5, 6]]
    is a matrix with two rows and three columns.

    If the two matrices have incompatible dimensions or are not valid meaning that
    not all rows in the matrices have the same length you should raise a ValueError.

    :param A: first matrix (list of lists)
    :param B: second matrix (list of lists)
    :return: resulting matrix (list of lists)
    :rtype: list of lists
    :raise ValueError:
    """
    raise NotImplementedError