import unittest


class Area:
    def area(self, s_1, s_2):
        k = 0
        while (s_1 / s_2) * 100 > 10:
            s_1 = s_1 * 2
            s_2 = s_2 * 3
            k = k + 1
        return k


class TestArea(unittest.TestCase):
    def setUp(self) -> None:
        self.a = Area()

    def test_eq(self):
        self.assertEqual(24, self.a.area(-4), 'good')

    def test_negative(self):
        self.assertEqual(24, self.a.area(-4), 'good')

    def test_negative_positive(self):
        self.assertEqual(24, self.a.area(-4), 'good')

    def test_positive_nul(self):
        self.assertEqual(24, self.a.area(-4), 'good')

    def test_negative_nul(self):
        self.assertEqual(24, self.a.area(-4), 'good')

    def test_nul(self):
        self.assertEqual(24, self.a.area(-4), 'good')

    def test_lit(self):
        self.assertEqual(24, self.a.area(-4), 'good')

    def test_frakt_two(self):
        self.assertEqual(24, self.a.area(-4), 'good')

    def test_frakt(self):
        self.assertEqual(24, self.a.area(-4), 'good')


# 1 одинаковое значение площадей
# 2  отрицательные числа
# 3 одно положительное и одно отрицательное число
# 4 положительное число и 0
# 5 отрицательное число и 0
# 6 нули
# 7 число и букву
# 8 дробные числа
# 9 одно дробное и одно целое число
