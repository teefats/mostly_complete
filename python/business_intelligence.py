def minimum_profitable_volume(sell_price, fixed_cost, cost_per_unit):
    """
    For this exercise, you will need to implement a function that
    computes the minimum number of units that need to be manufactured by a factory
    for their process to be profitable.

    We assume that every unit manufactured is sold at the sell_price.
    You will need to take into account the fixed_cost, which is a constant cost
    associated with manufactoring as well as the cost_per_unit that we have to pay for
    each unit manufactured.

    Your goal is to find how many units need to be built and sold
    in order for the total cost to be entirely covered by sales.

    E.g., minimum_profitable_volume(1020, 1000, 20) is 1
    E.g., minimum_profitable_volume(1019, 1000, 20) is 2
    E.g., minimum_profitable_volume(600, 1000, 20) is 2
    E.g., minimum_profitable_volume(30, 1000, 20) is 100
    E.g., minimum_profitable_volume(21, 1000, 20) is 1000

    Note: It isn't sustainable for the factory to sell a unit in a lower price than
    its manufacturing cost as it wouldn't make any profit. If that is the case and
    you cannot be profitable, return None.

    :param sell_price: price each unit is sold at
    :return: number of units that need to be made and sold
    :rtype: float | int
    """
    #Grab fixed cost and cost per unit
    def grab_fixed_cost(sell_price, fixed_cost, cost_per_unit):
        if cost_per_unit <= sell_price:
            profit = sell_price - cost_per_unit
            # print(profit)
            minimum_production = (fixed_cost + profit -1) //profit
            # print(minimum_production)
            if minimum_production <=0:
                minimum_production = None
                # print(minimum_production)

                return minimum_production
            else:
                print(minimum_production)
                return minimum_production
        else:
            minimum_production = None
            print(minimum_production)
            return minimum_production

    # def calc_min_volume(sell_price):
    #     minimum_production =grab_fixed_cost(fixed_cost, cost_per_unit)
    #     min_volume = minimum_production% sell_price
    #     print(min_volume)
    grab_fixed_cost(sell_price,fixed_cost, cost_per_unit)

    #Divide the total by the sell price
    # calc_min_volume(sell_price)
    #If the sell price is lower than the price then 
   
# minimum_profitable_volume(600, 1000, 20)
#minimum_profitable_volume(1020, 1000, 20) #is 1
#minimum_profitable_volume(1019, 1000, 20) #is 2
#minimum_profitable_volume(600, 1000, 20) #is 2
#minimum_profitable_volume(30, 1000, 20) #is 100
#minimum_profitable_volume(21, 1000, 20)# #is 1000