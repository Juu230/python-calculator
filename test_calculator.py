import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(87,13), 100)
        self.assertEqual(self.calc.add(0,0), 0)

    def test_substract(self):
        self.assertEqual(self.calc.subtract(5,2),3)
        self.assertEqual(self.calc.subtract(0,2),-2)
        self.assertEqual(self.calc.subtract(2,0),2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3,7),21)
        self.assertEqual(self.calc.multiply(30,0),0)
        self.assertEqual(self.calc.multiply(-1,8),-8)

    def test_divide(self):
        self.assertEqual(self.calc.divide(5,2),2)
        self.assertEqual(self.calc.divide(4,0),"can't divide")
        self.assertEqual(self.calc.divide(0,4),0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5,2),1)
        self.assertEqual(self.calc.modulo(5,2),1)
        self.assertEqual(self.calc.modulo(5,2),1)
    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()