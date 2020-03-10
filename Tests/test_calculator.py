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

if __name__ == '__main__':
    unittest.main()