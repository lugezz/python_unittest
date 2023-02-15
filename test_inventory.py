import unittest
from unittest.mock import patch

from inventory import Inventory, NotEnoughQuantity


class TestCalc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Run once at the beginning')

    @classmethod
    def tearDownClass(cls):
        print('Run once at the end')

    def setUp(self):
        print('\nRun at the beginning of each test')
        self.inv_1 = Inventory('Coke', 'Drink', 300, 20)
        self.inv_2 = Inventory('Phillip-Morris', 'Cigarettes', 350)

    def tearDown(self):
        print('Run at the end of each test')

    def test_code(self):
        print('test_code')
        self.assertEqual(self.inv_1.code, 'Drink-Coke')
        self.assertEqual(self.inv_2.code, 'Cigarettes-Phillip-Morris')

        self.inv_1.name = 'Pepsi'
        self.inv_2.name = 'Camel'

        self.assertEqual(self.inv_1.code, 'Drink-Pepsi')
        self.assertEqual(self.inv_2.code, 'Cigarettes-Camel')

    def test_inventory_cost(self):
        print('test_full_cost')
        self.assertEqual(self.inv_1.inventory_total_cost, 6000)
        self.assertEqual(self.inv_2.inventory_total_cost, 0)

        self.inv_1.quantity = 0
        self.inv_2.quantity = 100

        self.assertEqual(self.inv_1.inventory_total_cost, 0)
        self.assertEqual(self.inv_2.inventory_total_cost, 35000)
        
    def test_inventory_price(self):
        print('test_full_price')
        self.assertEqual(self.inv_1.inventory_total_price, 7800)
        self.assertEqual(self.inv_2.inventory_total_price, 0)

        self.inv_1.quantity = 0
        self.inv_2.quantity = 100

        self.assertEqual(self.inv_1.inventory_total_price, 0)
        self.assertEqual(self.inv_2.inventory_total_price, 45500)

    def test_apply_raise(self):
        print('test_apply_raise')
        self.inv_1.apply_raise()
        self.inv_2.apply_raise()

        self.assertEqual(self.inv_1.price, 429)
        self.assertEqual(self.inv_2.price, 500.5)
        
    def test_change_quantity(self):
        print('test_change_quantity')
        self.inv_1.increment_quantity(10)
        self.inv_2.increment_quantity(20)

        self.assertEqual(self.inv_1.quantity, 30)
        self.assertEqual(self.inv_2.quantity, 20)
        
        self.inv_1.decrease_quantity(10)
        
        self.assertEqual(self.inv_1.quantity, 20)
        self.assertRaises(NotEnoughQuantity, self.inv_2.decrease_quantity, 100)
        
    def test_mysystem(self):
        with patch('inventory.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            check_system = self.inv_1.check_system()
            mocked_get.assert_called_with('https://mysystem.com/Drink-Coke')
            self.assertEqual(check_system, 'Success')

            mocked_get.return_value.ok = False

            check_system = self.inv_2.check_system()
            mocked_get.assert_called_with('https://mysystem.com/Cigarettes-Phillip-Morris')
            self.assertEqual(check_system, 'Bad Response!')
                

if __name__ == '__main__':
    unittest.main()
