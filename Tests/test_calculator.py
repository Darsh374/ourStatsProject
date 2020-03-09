import unittest

from Calculator.Calculator import Calculator

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        add = self.calculator.add(4 ,6)
        self.assertEqual(add, 10)

    def test_subtraction(self):
        subtract = self.calculator.subtract(6 ,3)
        self.assertEqual(subtract, 3)