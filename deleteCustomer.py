#!/usr/bin/env python3
# encoding: utf-8

from dbutil import db_delete_records
from dbutil import db_read_records

#This function will remove given customer from db
def delete_customer(name):
    if db_read_records(name) != None:
        return db_delete_records(name)