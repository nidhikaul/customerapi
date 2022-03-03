#!/usr/bin/env python3
# encoding: utf-8

from dbutil import db_create_records
from dbutil import db_read_records

#Creating a new customer
def create_customer(name):
    if type(name) == str and not name.isnumeric() and len(name) != 0:
        if db_read_records(name) == None:
            return db_create_records(name)
    return None

