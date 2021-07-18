def derivative(w1, w2, x):
    """
    Given the following function f(x) = w1 * x^3 + w2 * x - 1
    evaluate the derivative of the function on x

    :param w1: first coefficient
    :param w2: second coefficient
    :param x: point on which to evaluate derivative (float)
    :return: value of the derivative on point x
    :rtype: float
    """
    n = 3
    formula_analysis = w1 * x**n + w2 * x-1
    derivative = float(((n *w1)* ((float(x))**(n-1))) + ((w2)))
    print(formula_analysis)
    print(derivative)
    return derivative
    # raise NotImplementedError

derivative(3,4,5)