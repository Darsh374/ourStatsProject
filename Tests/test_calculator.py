import unittest

from Calculator.Calculator import Calculator

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        add = self.calculator.add(2 ,2)
        self.assertEqual(add, 4)

    def test_subtraction(self):
        subtract = self.calculator.subtract(2 ,2)
        self.assertEqual(subtract, 0)

    def test_multiplication(self):
        product = self.calculator.product(3, 2)
        self.assertEqual(product, 6)

    def test_division(self):
        divide = self.calculator.divide(2, 1)
        self.assertEqual(divide, 2)

    def test_power(self):
        power = self.calculator.power(3, 2)
        self.assertEqual(power, 9)

    def test_root(self):
        root = self.calculator.root(16,2)
        self.assertEqual(root, 4)
        

if __name__ == '__main__':
    unittest.main()