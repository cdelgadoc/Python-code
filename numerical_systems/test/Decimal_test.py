import unittest
from numerical_systems.conversion.Decimal import Decimal


class TestDecimal(unittest.TestCase):

    def test_to_binary(self):
        self.assertEqual(Decimal.to_binary(10), '1010')
        self.assertEqual(Decimal.to_binary(15), '1111')

    def test_to_binary_zero(self):
        self.assertEqual(Decimal.to_binary(0), '0')

    def test_to_binary_builtin(self):
        self.assertEqual(Decimal.to_binary_builtin(10), '0b1010')
        self.assertEqual(Decimal.to_binary_builtin(-10), '-0b1010')

    def test_to_octal(self):
        self.assertEqual(Decimal.to_octal(10), 12)
        self.assertEqual(Decimal.to_octal(15), 17)

    def test_to_octal_zero(self):
        self.assertEqual(Decimal.to_octal(0), '0')

    def test_to_octal_builtin(self):
        self.assertEqual(Decimal.to_octal_builtin(10), 12)
        self.assertEqual(Decimal.to_octal_builtin(-10), 12)

    def test_to_hexadecimal(self):
        self.assertEqual(Decimal.to_hexadecimal(10), 'A')
        self.assertEqual(Decimal.to_hexadecimal(15), 'F')

    def test_to_hexadecimal_zero(self):
        self.assertEqual(Decimal.to_hexadecimal(0), '0')

    def test_to_hexadecimal_builtin(self):
        self.assertEqual(Decimal.to_hexadecimal_builtin(10), 'a')
        self.assertEqual(Decimal.to_hexadecimal_builtin(-10), 'a')


if __name__ == '__main__':
    unittest.main()
