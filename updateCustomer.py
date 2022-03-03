#!/usr/bin/env python3
# encoding: utf-8

from cartCheckout import calCost
from dbutil import db_update_records
from dbutil import db_read_records

def purchase_item(name): 
    result = db_read_records(name)
    # Check if the customer exists in db
    if result != None:
        price = calCost(name, 100)
        count = result[name] 
        # If yes increment count by 1
        result[name] += 1
        db_update_records(name, result[name])
        # Calculate price after discount
        return {name: count, "price": price}
    return {"error": "Enter a name"}