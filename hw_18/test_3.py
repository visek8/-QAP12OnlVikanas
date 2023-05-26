import unittest


class Multiplication:
    def prod(self, n):
        p = 1
        while n > 0:
            p = p * n
            n = n - 1
        return p


class TestMult(unittest.TestCase):
    def setUp(self) -> None:
        self.m = Multiplication()

    def test_negative(self):
        self.assertEqual(24, self.m.prod(-4), 'good')

    def test_nul(self):
        self.assertEqual(0, self.m.prod(0), 'good')

    def test_min(self):
        self.assertEqual(0.88, self.m.prod(0.5), 'good')

    def test_frakt(self):
        self.assertEqual(2, self.m.prod(2.5), 'good')

    def test_lit(self):
        self.assertEqual(24, self.m.prod(4), 'good')

    def test_simbl(self):
        self.assertEqual(24, self.m.prod('!'), 'good')

    def test_plus(self):
        self.assertEqual(24, self.m.prod(+4), 'good')

    def test_ten(self):
        self.assertEqual('Error', self.m.prod(1000000000), 'good')

# 1 отрицательное число
# 2 0
# 3 дробное число больше 0 но меньше 1
# 4  любое дробное число
# 5  букву
# 6  спец символ
# 7  положительное число со знаком плюса перед ним
# 8 10-значное число
