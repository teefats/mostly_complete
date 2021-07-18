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

def flip_prices(prices):
    """
    This function returns a list of daily prices for each observed hour given
    a list of hourly prices for each observed day.

    E.g., 

    NOTE: prices need to consist of lists of the same length meaning that no prices
    for given hours are missing and if they are, you must raise a ValueError.

    :param prices: list (for days) of list (for hours) of prices
    :return: list (for hours) of list (for days) of prices
    :rtype: list
    """
    def confirm_num_list(prices): 
        for daily_price in prices:
            first_day_price = len(prices[0])

            len_daily_price = len(daily_price)
            if first_day_price != len_daily_price:
                raise ValueError
            else:
                continue

    def flip_list(prices):
        index = 0
        first_day =[]
        second_day = []
        third_day =[]
        # #for daily_prices in prices:
        # for count, daily_price in enumerate(prices, start=0):
        #     print(daily_price[count])
        for daily_price in prices:
            first_hour =daily_price[0]
            # print(hours)
            # index +=1
            second_hour = daily_price[1]
            third_hour = daily_price[2]

            first_day.append(first_hour)
            second_day.append(second_hour)
            third_day.append(third_hour)


            print(daily_price)
        print(first_day)
        print(second_day)
        price_list = [first_day, second_day,third_day]
        print(price_list)


    flip_list(prices)


flip_prices(PRICES_PER_HOUR_PER_DAY_SAMPLE) #is [[1, 4], [2, 5], [3, 6]]  
