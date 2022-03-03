import unittest
import dbutil
from addCustomer import create_customer
from deleteCustomer import delete_customer
from getCustomer import get_customer

class TestDeleteCustomer(unittest.TestCase):
    #Initialize new db file, create records
    def setUp(self):
        dbutil.db_initialize()
        dbutil.db_create_records('rose')
        # dbutil.db_delete_records('rose')


    #Pass if fetching nonexisting cust = None
    def test_nonexisting_customer(self):
        self.assertEqual(delete_customer('rose'), {'deleted': 'rose'})
        self.assertEqual(get_customer('rose'), None)

    # Wipe the test db file.
    # def tearDown(self):
    #     dbutil.db_initialize()


if __name__ == '__main__':
    unittest.main()