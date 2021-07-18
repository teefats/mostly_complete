from flip_prices import PRICES_PER_HOUR_PER_DAY_SAMPLE
 
 
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

    # def flip_list(prices):
    #     index = 0
    #     first_day =[]
    #     second_day = []
    #     third_day =[]
    #     # #for daily_prices in prices:
    #     # for count, daily_price in enumerate(prices, start=0):
    #     #     print(daily_price[count])
    #     for daily_price in prices:
    #         first_hour =daily_price[0]
    #         # print(hours)
    #         # index +=1
    #         second_hour = daily_price[1]
    #         third_hour = daily_price[2]

    #         first_day.append(first_hour)
    #         second_day.append(second_hour)
    #         third_day.append(third_hour)


    #         print(daily_price)
    #     print(first_day)
    #     print(second_day)
    #     price_list = [first_day, second_day,third_day]
    #     print(price_list)
    def flip_lists(prices):

        daily_prices = []
        
        
        for i in range(len(prices)+1):
            for daily_price in prices:
                daily_prices.append(daily_price[i])
                #print(daily_price[i])

        # print(daily_prices)
        index= 0
        # daily_prices =[[x] for x in daily_prices]
        # print(daily_prices)
        
        print(f'{daily_prices}djfjf')

        #for index, daily_price in prices:
            #print(daily_price[index])
            #index +=1

    print("N")
    flip_lists(prices)


flip_prices([[1, 2, 3], [4, 5, 6]]) #is [[1, 4], [2, 5], [3, 6]]  
