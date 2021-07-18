"""
DATA PROCESSING

DO NOT MODIFY CONSTANTS
"""





PRICES_PER_HOUR_PER_DAY_SAMPLE = [
    [
        11300,
        12000,
        12100,
        12100,
        11800,
        11100,
        10300,
        9400,
    ],  # Prices for business hours on Monday
    [
        10100,
        10300,
        10200,
        10300,
        10200,
        10100,
        10200,
        10200,
    ],  # Prices for business hours on Tuesday
    [
        10600,
        10700,
        10100,
        10000,
        9800,
        8400,
        7500,
        9000,
    ],  # Prices for business hours on Wednesday
    [
        9100,
        9600,
        10200,
        10200,
        10200,
        10300,
        10100,
        10400,
    ],  # Prices for business hours on Thursday
    [
        10500,
        10600,
        13200,
        10800,
        10500,
        10200,
        9900,
        9800,
    ],  # Prices for business hours on Friday
]


def normalize_prices(prices):
    """
    This function takes a list of prices for a given commodity.

    The prices are given as a list of list of numbers. Each inner list corresponds
    to a day of the week, and each number corresponds to the price at a given
    hour of the day (limited to business hours only).

    See the example of PRICES_PER_HOUR_PER_DAY_SAMPLE above. Here we have a list
    containing five lists (so the data is for one week only), each inner list
    contains 8 numbers, for 8 hours in the day.

    This function should normalise all the prices such that the first value is
    worth 100 and the other are adjusted accordingly.

    E.g., normalize_prices([[1, 2], [3, 4]]) is [[100, 200], [300, 400]]
    E.g., normalize_prices([[200, 20], [30, 400]]) is [[100, 10], [15, 200]]

    NOTE: prices need to consist of lists of the same length meaning that no prices
    for given hours are missing and if they are, you must raise a ValueError.

    :param prices: list of list of prices
    :return: normalised list of list of prices where the first price is 100
    and the other prices are scaled accordingly
    :rtype: list
    """
    #Calculate the normalisation factor

    #Normalise all the others by this factor


    #Replace the first character with 100

    #return the list

    def determine_norm(prices):
        first_hour_price = prices[0][0]
        #print(first_hour_price)#
        factor = (first_hour_price/100)
        # print(factor)
        return factor
    
    # def check_size_of_list(prices):
    #     for daily_price in prices:
            #if len

    # def check_num_lists(daily_price):

    #     len_list = len(daily_price)
    #     if len_list == 8:
    #         return daily_price
    #     else:
    #         raise ValueError

    def confirm_num_list(prices):
        for daily_price in prices:
            first_day_price = len(prices[0])

            len_daily_price = len(daily_price)
            if first_day_price != len_daily_price:
                raise ValueError
            else:
                continue
            

    def normalise(prices):
        new =[]
        for daily_price in prices:
            #daily_price = check_num_lists(daily_price)
            confirm_num_list(prices)
            factor = determine_norm(prices)
            new_daily = [int(hourly/factor) for hourly in daily_price]
            new.append(new_daily)
                #new_list = 
        print(new)

    normalise(prices)


normalize_prices(PRICES_PER_HOUR_PER_DAY_SAMPLE) #is [[100, 10], [15, 200]]


# list = [3,4,5,3,54]
# num = 4
# new_list = [i /num for i in list]
# print(new_list)