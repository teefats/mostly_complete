from probabilities import bin_dist


def bin_cdf(n, p, x):
    """
    Given n number of trials, p the probability of successes,
    what is the probability of having less than or equal to x successes?

    Your function should raise a ValueError if x is higher
    than n.

    :param n: number of trials (int)
    :param p: probability of success
    :param x: number of successes (int)
    :return: probability of having less than or
    equal to x successes
    :rtype: float
    :raise ValueError: if x > n
    """

    # p C (bin_dist) ** 0 ) *(1-bin_dist)** p

    # n = (p)=20
    # x = x = 1 = r
    # nCr = n! / r!(n-r)

    








    def bin_dist(n, p, x):
        """
    Given n number of trials, p the probability of success,
    what is the probability of having x successes?

    Your function should raise a ValueError if x is higher
    than n.

    If you need to compute combinations, you can import the
    function "comb" from the package "scipy.special"

    :param n: number of trials (int)
    :param p: probability of success
    :param x: number of successes (int)
    :return: probability of having x successes
    :rtype: float
    :raise ValueError: if x > n
    """
        def factorial(x):
            if x >= 0:
                    
                factorial = 1

                for i in range(1, x + 1):
                    factorial = float(factorial * i)
                # print(f' The factorial of {x} is {factorial}') 
                return factorial

            else:
                raise ValueError("Sorry x cannot be a negative number")

        def combination(n, r):
            """
            Given n total number of items,
            what is the number of possible ways
            to choose r items from it?

            :param n: total number of items (integer)
            :param r: number of items to arrange (int)
            :return: number of combinations
            :rtype: integer
            """

            

            
            numerator = factorial(n)
            denominator = factorial(r)
            subtracted_answer = factorial(n-r)
            

            answer = numerator/(denominator * subtracted_answer)
            print(answer)
            return answer 

        # from scipy.special import comb
        if x > n:
            raise ValueError("Error, x must be less than n")
        else:


            prob_success = float((combination(n, x)) * ((p**x)*((1-p)**(n-x))))

            print(prob_success)
            return prob_success 
    
    # an= 1-bin_dist(n,p,x)
    # print(f'word{an}')
    # n= 12
    # p=0.25
    # # x=0??
    # ((n!)/ (x!*(n-x)!)) * (p**x) * (1-p)**(n-x)
    sum_prob = []
    for i in range(x+1):
        print(i)
        prob = bin_dist(n,p,x=i)
        sum_prob.append(prob)
    print(sum_prob)
    total =sum(sum_prob)
    print(total)

bin_cdf(12,0.245,3)





