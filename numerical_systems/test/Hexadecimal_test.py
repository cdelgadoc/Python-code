import unittest
from numerical_systems.conversion.Hexadecimal import Hexadecimal


class TestHexadecimal(unittest.TestCase):

    def test_to_decimal_builtin(self):
        self.assertEqual(Hexadecimal.to_decimal_builtin('A'), 10)
        self.assertEqual(Hexadecimal.to_decimal_builtin('FF'), 255)

    def test_to_decimal(self):
        self.assertEqual(Hexadecimal.to_decimal('A'), 10)
        self.assertEqual(Hexadecimal.to_decimal('FF'), 255)


if __name__ == '__main__':
    unittest.main()
