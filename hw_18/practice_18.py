from unittest import TestCase


class Calculator:
    def sum(self, a, b):
        try:
            return float(a) + float(b)
        except:
            return 0

    def delete(self, a, b):
        return a / b


class TestCalculator(TestCase):
    def setUp(self) -> None:
        self.culk = Calculator()

    def test_sum_1(self):
        self.assertEqual(0, self.culk.sum(0, 0), 'Sum != 0')

    def test_sum_symbols(self):
        self.assertEqual(0, self.culk.sum('a', 'b'), 'Summ symbols != 0')
    def test_sum_25(self):
        self.assertEqual(25, self.culk.sum(12, 13), 'Summ symbols != 0')
    def test_sum_2000(self):
        self.assertEqual(0, self.culk.sum(1000.1, 1000.1), 'Summ symbols != 0')