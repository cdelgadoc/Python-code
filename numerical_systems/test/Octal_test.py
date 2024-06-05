import unittest
from numerical_systems.conversion.Octal import Octal


class TestOctal(unittest.TestCase):

    def test_to_decimal_builtin(self):
        self.assertEqual(Octal.to_decimal_builtin('10'), 8)
        self.assertEqual(Octal.to_decimal_builtin('777'), 511)

    def test_to_decimal(self):
        self.assertEqual(Octal.to_decimal('10'), 8)
        self.assertEqual(Octal.to_decimal('777'), 511)


if __name__ == '__main__':
    unittest.main()
