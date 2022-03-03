# - Has an API for a customer to make a purchase.
# - Tracks the number of purchases made by a customer.
# - Returns the cost of the purchase.
# - Cost is $100 minus a loyalty discount.

from dbutil import db_read_records

#Calculating the discount as per the purchase count
def calCost(name, base_price):
    record = db_read_records(name)
    if record != None:
        purchase_count = record[name]
        if purchase_count == 0:
            discount = 0
        elif purchase_count in range(1,3): 
            discount = 0.01
        elif purchase_count in range(3,6):
            discount = 0.02
        elif purchase_count in range(5,11):
            discount = 0.05
        elif purchase_count > 10:
            discount = 0.1
    discounted_cost = base_price * ( 1 - discount)
    return discounted_cost
