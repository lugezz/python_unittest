import unittest

import arythmetic


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(arythmetic.add(10, 5), 15)
        self.assertEqual(arythmetic.add(-10, 5), -5)
        self.assertEqual(arythmetic.add(-1, -2), -3)
        self.assertEqual(arythmetic.add(999999.99, 0.01), 1000000)
        
    def test_substract(self):
        self.assertEqual(arythmetic.subtract(10, 5), 5)
        self.assertEqual(arythmetic.subtract(-10, 5), -15)
        self.assertEqual(arythmetic.subtract(-1, -2), 1)
        self.assertEqual(arythmetic.subtract(999999.99, 0.01), 999999.98)
        
    def test_multiply(self):
        self.assertEqual(arythmetic.multiply(10, 5), 50)
        self.assertEqual(arythmetic.multiply(-10, 5), -50)
        self.assertEqual(arythmetic.multiply(-1, -2), 2)
        self.assertEqual(arythmetic.multiply(999999.99, 0.01), 9999.9999)
        
    def test_divide(self):
        self.assertEqual(arythmetic.divide(10, 4), 2.5)
        self.assertEqual(arythmetic.divide(-10, 4), -2.5)
        self.assertEqual(arythmetic.divide(-1, -2), 0.5)
        self.assertEqual(arythmetic.divide(999999.99, 0.01), 99999999)
        self.assertRaises(ValueError, arythmetic.divide, 10, 0)
        

if __name__ == '__main__':
    unittest.main()
