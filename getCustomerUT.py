import unittest
from getCustomer import get_customer
import dbutil

class TestGetCustomer(unittest.TestCase):

#Initializing the db for test case
    def setUp(self):
        dbutil.db_initialize()
        dbutil.db_create_records('edsel')

#Test Case : query non existing customer
    def test_nonexisting_customer(self):
        self.assertEqual(get_customer('alice'), None)

    def test_existing_customer(self):
        self.assertNotEqual(get_customer('edsel'),None)

# Clear test db for this function.
    def tearDown(self):
        dbutil.db_initialize()

if __name__ == '__main__':
    unittest.main()