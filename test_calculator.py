import unittest

from calculator import add, subtract, multiply, divide


class CalculatorSecurityTests(unittest.TestCase):
    def test_divide_by_zero_rejected(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_basic_operations_unchanged(self):
        self.assertEqual(add(5, 2), 7)
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(multiply(5, 2), 10)
        self.assertEqual(divide(10, 2), 5)


if __name__ == "__main__":
    unittest.main()
