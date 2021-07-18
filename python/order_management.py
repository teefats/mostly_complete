"""
ORDER AND CART MANAGEMENT

Orders are sets of items ordered by a customer
An ordered item has four components:
 - a name
 - a quantity (the number of such items bought)
 - a unit price (in pence)
 - a unit weight (in pounds)
Those are represented by a tuple.

NOTE: You can safely assume that all orders have all the required fields
(name, quantity, unit-price and unit-weight) so no validation needs to be made.

DO NOT MODIFY CONSTANTS
"""

ORDER_SAMPLE_1 = {("lamp", 2, 2399, 2), ("chair", 4, 3199, 10), ("table", 1, 5599, 85)}
ORDER_SAMPLE_2 = {("sofa", 1, 18399, 140), ("bookshelf", 2, 4799, 40)}

CATALOGUE = {("table", 9999, 20), ("chair", 2999, 5), ("lamp", 1999, 10)}


def delivery_charges(order):
    """
    Compute the delivery charges for an order. The company charges a flat £50
    fee plus £20 for each 100lbs (additional weight under 100lbs is ignored).

    E.g., delivery_charges({("desk", 1, 11999, 160)}) is 7000 (pence)
    E.g., delivery_charges({("desk", 2, 11999, 160)}) is 11000 (pence)
    E.g., delivery_charges({("lamp", 1, 2399, 2)}) is 5000 (pence)
    E.g., delivery_charges({("lamp", 50, 2399, 2)}) is 7000 (pence)

    :param order: order to process. See samples for examples.
    :return: delivery fee in pence
    :rtype: float | int
    """
    def extract_deliverycharge(quantity, weight):
        total_weight = quantity * weight
        flat_fee = 50
        if total_weight < 100:
            total_fee = flat_fee *100.00
            print(total_fee)
            return total_fee
        else:
            
            total_fee = (((total_weight//100)*20) + flat_fee)*100
            print(total_fee)
            return total_fee
        
  

        


    total_delivery = 0
    for item in order:
        name =item[0]
        quantity = item[1]
        price =item[2]
        weight =item[3]
        
        total_delivery += extract_deliverycharge(quantity, weight)
        # total_delivery += total_fee
    print(total_delivery)


delivery_charges(order=ORDER_SAMPLE_2)

