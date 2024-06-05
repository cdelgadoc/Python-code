import unittest
from numerical_systems.conversion.Binary import Binary


class TestBinary(unittest.TestCase):
    def test_is_binary_valid(self):
        self.assertTrue(Binary.is_binary('101010'))
        self.assertTrue(Binary.is_binary('1111'))
        self.assertTrue(Binary.is_binary('0'))

    def test_is_binary_invalid(self):
        self.assertFalse(Binary.is_binary('1234'))
        self.assertFalse(Binary.is_binary('102'))
        self.assertFalse(Binary.is_binary('2'))
        self.assertFalse(Binary.is_binary(''))

    def test_to_decimal(self):
        self.assertEqual(Binary.to_decimal('101010'), 42)
        self.assertEqual(Binary.to_decimal('1111'), 15)
        self.assertEqual(Binary.to_decimal('0'), 0)

    def test_to_decimal_builtin(self):
        self.assertEqual(Binary.to_decimal_builtin('101010'), 42)
        self.assertEqual(Binary.to_decimal_builtin('1111'), 15)
        self.assertEqual(Binary.to_decimal_builtin('0'), 0)

    def test_to_octal(self):
        self.assertEqual(Binary.to_octal('101010'), '52')
        self.assertEqual(Binary.to_octal('1111'), '17')
        self.assertEqual(Binary.to_octal('0'), '0')

    def test_to_hexadecimal(self):
        self.assertEqual(Binary.to_hexadecimal('101010'), '2a')
        self.assertEqual(Binary.to_hexadecimal('1111'), 'f')
        self.assertEqual(Binary.to_hexadecimal('0'), '0')


if __name__ == '__main__':
    unittest.main()
