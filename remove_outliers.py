def remove_outliers(data):
    """
    Given a list of numbers, find outliers and return a new
    list that contains all points except outliers
    We consider points lying outside 2 standard
    deviations from the mean.

    Make sure that you do not modify the original list!

    If data is empty raise a ValueError

    :param data: list of numbers
    :return: a new list without outliers
    :rtype: list
    :raise ValueError:
    """
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
    def standard(data):
        variances= []
        for i in data:
            deviation = (i - mean_calc(data))**2
            variances.append(deviation)
        variance = mean_calc(variances)
        print(variance)
        standard_deviation = round((variance**0.5),2)
        print(standard_deviation)

        
        return standard_deviation

    outliers = []
    clean_list =[]
    
    upper_sd = mean_calc(data) + (2*(standard(data)))
    print(f'upper {upper_sd}')
    lower_sd = mean_calc(data) - (2*(standard(data)))
    print(f'upper {upper_sd}')
    print(f' Lower sd {lower_sd}')
    for i in data:
        print(f'Numbers...{i}')
        if not(i >= upper_sd or i <= lower_sd):
            clean_list.append(i)
    print(clean_list)
    print(f'length of cleaned_list {len(clean_list)}')
    return clean_list

remove_outliers(data=[10, 386, 479, 627, 20, 523, 482, 483, 542, 699, 535, 617, 577, 471, 615, 583, 441, 562, 563, 527, 453, 530, 433, 541, 585, 704, 443, 569, 430, 637, 331, 511, 552, 496, 484, 566, 554, 472, 335, 440, 579, 341, 545, 615, 548, 604, 439, 556, 442, 461, 624, 611, 444, 578, 405, 487, 490, 496, 398, 512, 422, 455, 449, 432, 607, 679, 434, 597, 639, 565, 415, 486, 668, 414, 665, 763, 557, 304, 404, 454, 689, 610, 483, 441, 657, 590, 492, 476, 437, 483, 529, 363, 711, 543])

# dark= [386, 479, 627, 523, 482, 483, 542, 699, 535, 617, 577, 471, 615, 583, 441, 562, 563,
#    527, 453, 530, 433, 541, 585, 704, 443, 569, 430, 637, 331, 511, 552, 496, 484, 566,
#    554, 472, 335, 440, 579, 341, 545, 615, 548, 604, 439, 556, 442, 461, 624, 611, 444,
#    578, 405, 487, 490, 496, 398, 512, 422, 455, 449, 432, 607, 679, 434, 597, 639, 565,
#    415, 486, 668, 414, 665, 557, 304, 404, 454, 689, 610, 483, 441, 657, 590, 492, 476,
#    437, 483, 529, 363, 711, 543]
# print(f' dark chocolate {len(dark)}')