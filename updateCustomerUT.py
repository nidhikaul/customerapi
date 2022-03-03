import unittest
import dbutil
from updateCustomer import purchase_item


class TestPutCustomer(unittest.TestCase):
    #Helper function to generate the purchase count
    def buy_item(self, count):
        for i in range(count):
            purchase_item('edsel')

    def setUp(self):
        dbutil.db_initialize()
        dbutil.db_create_records('edsel')

    def test_existing_customer(self):
        self.assertEqual(purchase_item('edsel'), {"edsel": 0, "price": 100})

    # Test cases to evaluate all the discount levels
    def test_discount1_customer(self):
        self.buy_item(1)
        self.assertEqual(purchase_item('edsel'), {"edsel": 1, "price": 99})

    def test_discount2_customer(self):
        self.buy_item(3)
        self.assertEqual(purchase_item('edsel'), {"edsel": 3, "price": 98})
        
    def test_discount5_customer(self):
        self.buy_item(6)
        self.assertEqual(purchase_item('edsel'), {"edsel": 6, "price": 95.0})

    def test_discount10_customer(self):
        self.buy_item(11)
        self.assertEqual(purchase_item('edsel'), {"edsel": 11, "price": 90.0})
        
    def test_discount4_customer(self):
        self.buy_item(100)
        self.assertEqual(purchase_item('edsel'), {"edsel": 100, "price": 90.0})

    # Testing a fail case
    def test_discount_fail_customer(self):
        self.buy_item(1)
        self.assertNotEqual(purchase_item('edsel'), {"edsel": 1, "price": 100})

    # Wipe the test db file.
    # def tearDown(self):
    #     dbutil.db_initialize()

if __name__ == '__main__':
    unittest.main()