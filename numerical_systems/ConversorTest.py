import unittest
from Conversor import Conversor


class ConversorTest(unittest.TestCase):

    def test_is_binary(self):
        self.assertTrue(Conversor.is_binary("101010"))
        self.assertTrue(Conversor.is_binary("1100101"))
        self.assertFalse(Conversor.is_binary("12345"))
        self.assertFalse(Conversor.is_binary("01012"))

    def test_binary_to_decimal(self):
        self.assertEqual(Conversor.binary_to_decimal("1010"), 10)
        self.assertEqual(Conversor.binary_to_decimal("1101"), 13)
        self.assertIsNone(Conversor.binary_to_decimal("1234"))
        self.assertIsNone(Conversor.binary_to_decimal(""))

    def test_binary_to_octal(self):
        self.assertEqual(Conversor.binary_to_octal("1010"), "12")
        self.assertEqual(Conversor.binary_to_octal("1101"), "15")
        self.assertIsNone(Conversor.binary_to_octal("1234"))
        self.assertIsNone(Conversor.binary_to_octal(""))

    def test_binary_to_hexadecimal(self):
        self.assertEqual(Conversor.binary_to_hexadecimal("1010"), "A")
        self.assertEqual(Conversor.binary_to_hexadecimal("1101"), "D")
        self.assertIsNone(Conversor.binary_to_hexadecimal("1234"))
        self.assertIsNone(Conversor.binary_to_hexadecimal(""))

    def test_decimal_to_binary(self):
        self.assertEqual(Conversor.decimal_to_binary(10), "1010")
        self.assertEqual(Conversor.decimal_to_binary(13), "1101")
        self.assertIsNone(Conversor.decimal_to_binary(-1))
        self.assertEqual(Conversor.decimal_to_binary(0), "0")

    def test_decimal_to_octal(self):
        self.assertEqual(Conversor.decimal_to_octal(10), "12")
        self.assertEqual(Conversor.decimal_to_octal(13), "15")
        self.assertIsNone(Conversor.decimal_to_octal(-1))
        self.assertEqual(Conversor.decimal_to_octal(0), "0")

    def test_decimal_to_hexadecimal(self):
        self.assertEqual(Conversor.decimal_to_hexadecimal(10), "A")
        self.assertEqual(Conversor.decimal_to_hexadecimal(13), "D")
        self.assertIsNone(Conversor.decimal_to_hexadecimal(-1))
        self.assertEqual(Conversor.decimal_to_hexadecimal(0), "0")

    def test_octal_to_decimal(self):
        self.assertEqual(Conversor.octal_to_decimal("12"), 10)
        self.assertEqual(Conversor.octal_to_decimal("15"), 13)
        self.assertEqual(Conversor.octal_to_decimal("0"), 0)

    def test_to_decimal_builtin(self):
        self.assertEqual(Conversor.to_decimal_builtin("A"), 10)
        self.assertEqual(Conversor.to_decimal_builtin("D"), 13)
        self.assertEqual(Conversor.to_decimal_builtin("0"), 0)


if __name__ == '__main__':
    unittest.main()
