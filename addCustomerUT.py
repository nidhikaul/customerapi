import unittest
import dbutil
from addCustomer import create_customer
from getCustomer import get_customer

class TestPostCustomer(unittest.TestCase):
    #Initialize new db file, create records
    def setUp(self):
        dbutil.db_initialize()
        dbutil.db_create_records('jelly')

    #Pass if the customer doesnt exist
    def test_nonexisting_customer(self):
        self.assertEqual(get_customer('alice'), None)

    #Fail if the customer gets created
    def test_add_customer(self):
        self.assertEqual(create_customer(''),None) # Check this

    #Fail if the type is anything other than strings
    def test_name_is_string(self):
      self.assertEqual(create_customer(123), None)

    # Wipe the test db file.
    # def tearDown(self):
    #     dbutil.db_initialize()


if __name__ == '__main__':
    unittest.main()