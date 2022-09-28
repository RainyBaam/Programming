import unittest
from two_sum import *
from main import calculate, standard_deviation, convert_precision


class MyTestCase(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(calculate(1.0, 4, '*'), 4)  # Проверка операции умножения

    def test_sum(self):
        self.assertEqual(calculate(1, 2, "+"), 3)

    def test_divide(self):
        self.assertEqual(calculate(7, 3, "//"), 2)

    def test_mod(self):
        self.assertEqual(calculate(9, 2, "%"), 1)

    def test_standard_deviation(self):
        self.assertEqual(standard_deviation(45, 45, 32, 65, 999, precision=0.00001), 381.04614)

    def test_cp_with_1(self):
        self.assertEqual(convert_precision('0.1'), 1, "Должна быть 1")

    def test_cp_with_2(self):
        self.assertEqual(convert_precision('0.01'), 2, "Должно быть 2")

    def test_cp_with_5(self):
        self.assertEqual(convert_precision('0.00001'), 5, "Должно быть 5")

    def test_cp_with_5_as_float(self):
        self.assertEqual(convert_precision(0.00001), 5, "Должно быть 5")

class TwoSumTestCase(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(two_sum(lst, target), (0, 6), "Базовый тестовый набор (test case)")

    def test_two_sum2(self):
        self.assertEqual(two_sum([1, 1, 2, 3], 2), (0, 1), "test case #2")

    def test_two_sum3(self):
        self.assertEqual(two_sum(list(range(1000000)), 999999), (0, 999999))

if __name__ == '__main__':
    unittest.main()
