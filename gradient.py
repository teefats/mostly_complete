def gradient(w1, w2, x):
    x1, x2 = x
    gradx1=2*w1*x1 + w2 * x2
    gradx2= w2 + w1 * x1 ** 2
    print(gradx1, gradx2)
    return (gradx1, gradx2)
# raise NotImplementedError

gradient(4,24,(4,9))

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