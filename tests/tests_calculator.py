# testes automatizados, depois mudar para receber arquivos txt

import unittest
from src.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        
    def test_simple_addition(self):
        self.assertEqual(self.calc.evaluate_postfix("3 4 +"), 7)
    
    def test_complex_expression(self):
        self.assertEqual(self.calc.evaluate_postfix("3 4 + 2 * 7 /"), 2.0)

    def test_invalid_expression(self):
        with self.assertRaises(ValueError):
            self.calc.evaluate_postfix("3 +")

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.evaluate_postfix("3 0 /")

if __name__ == "__main__":
    unittest.main()