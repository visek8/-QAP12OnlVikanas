import unittest


class Area:
    def area(self, s_1, s_2):
        k = 0
        if type(s_1) and type(s_2) not in [int]:
            raise TypeError('It`s not an integer number')
        if s_1 and s_2 < 0:
            raise ValueError('Error')
        if s_1 == 0 or s_2 == 0:
            raise ValueError('Area cannot be zero')
        while (s_1 / s_2) * 100 > 10:
            s_1 = s_1 * 2
            s_2 = s_2 * 3
            k = k + 1
        return k


class TestArea(unittest.TestCase):
    def setUp(self) -> None:
        self.a = Area()

    def test_eq(self):
        self.assertEqual(6, self.a.area(2, 2), 'good')

    def test_negative(self):
        self.assertEqual('Error', self.a.area(-2, -2), 'good')

    def test_negative_positive(self):
        self.assertEqual('Error', self.a.area(2, -2), 'good')

    def test_positive_nul(self):
        self.assertEqual('Area cannot be zero', self.a.area(2, 0), 'good')

    def test_negative_nul(self):
        self.assertEqual('Area cannot be zero', self.a.area(-2, 0), 'good')

    def test_nul(self):
        self.assertEqual('Area cannot be zero', self.a.area(0, 0), 'good')

    def test_lit(self):
        self.assertEqual('It`s not an integer number', self.a.area(2, 'a'), 'good')

    def test_frakt_two(self):
        self.assertEqual('It`s not an integer number', self.a.area(2.2, 3.2), 'good')

    def test_frakt(self):
        self.assertEqual('It`s not an integer number', self.a.area(2, 3.2), 'good')


# 1 одинаковое значение площадей
# 2  отрицательные числа
# 3 одно положительное и одно отрицательное число
# 4 положительное число и 0
# 5 отрицательное число и 0
# 6 нули
# 7 число и букву
# 8 дробные числа
# 9 одно дробное и одно целое число
