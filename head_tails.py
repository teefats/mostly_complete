def head_tails(p, n):
    """
    Given a coin that have probability p of giving a heads
    in each toss independently, what is the probability of
    having n heads consecutively in a row?

    :param p: probability of a head
    :param n: number of heads in a row (int)
    :return: probability of having n heads in a row
    :rtype: float
    """

    prob_heads = round((float(p**n)),5)
    print(prob_heads)
    return prob_heads

    
head_tails(0.5, 7)