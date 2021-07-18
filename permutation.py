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

    def factorial(x):
        if x >= 0:
                
            factorial = 1

            for i in range(1, x + 1):
                factorial = float(factorial * i)
            # print(f' The factorial of {x} is {factorial}') 
            return factorial

        else:
            raise ValueError("Sorry x cannot be a negative number")

    
    numerator = factorial(n)
    denominator = factorial(r)
    subtracted_answer = factorial(n-r)
    

    answer = numerator/(denominator * subtracted_answer)
    print(answer)
    return answer
    
combination(5,3)