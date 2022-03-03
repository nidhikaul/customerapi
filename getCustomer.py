#!/usr/bin/env python3
# encoding: utf-8

from dbutil import db_read_records

#Get existing customer details
def get_customer(name):
    return db_read_records(name)