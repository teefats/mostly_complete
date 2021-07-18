def calculate_mean(data):
    """
    Return the mean of a python list

    If data is empty raise a ValueError

    :param data: a list of numbers
    :return: the mean of the list
    :rtype: float
    :raise ValueError:
    """
    if len(data)== 0:
        raise ValueError("Data cannot be empty")
    else:

        sum_list = sum(data)
        len_list = len(data)
        mean_list = round(float((sum_list/ len_list)),2)

        print(mean_list)
        return mean_list


calculate_mean(data=[4,5,34,5])
   