def calculate_standard_deviation(data):
    """
    Return the standard deviation of a python list using the
    population size (N) in order to calculate the variance.

    If data is empty raise a ValueError

    :param data: list of numbers
    :return: the standard deviation of the list
    :rtype: float
    :raise ValueError:
    """

    def mean_calc(data):
        if len(data)== 0:
            raise ValueError("Data cannot be empty")
        else:

            sum_list = sum(data)
            len_list = len(data)
            mean_list = round(float((sum_list/ len_list)),2)

            print(mean_list)
            return(mean_list)
    variances= []
    for i in data:
        deviation = (i - mean_calc(data))**2
        variances.append(deviation)
    variance = mean_calc(variances)
    print(variance)
    standard_deviation = round((variance**0.5),2)
    print(standard_deviation)

    
    return standard_deviation





    
calculate_standard_deviation(data=[])