import unittest


class Sum:

    def fun(self, a, b, s):
        try:
            for i in range(a, b + 1):
                s = s + i
            return s
        except TypeError:
            print('Error')


class TestSum(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Sum()

    def test_negative(self):
        self.assertEqual(0, self.s.fun(1, -3, 0), 'good')

    def test_negative_double(self):
        self.assertEqual(0, self.s.fun(-1, -3, 0), 'good')

    def test_positive(self):
        self.assertEqual(6, self.s.fun(1, 3, 0), 'good')

    def test_a_bigger(self):
        self.assertEqual(0, self.s.fun(3, 1, 0), 'good')

    def test_eq(self):
        self.assertEqual(1, self.s.fun(1, 1, 0), 'good')

    def test_simb(self):
        self.assertEqual('Error', self.s.fun(1, 'a', 0), 'good')

    def test_frak_2(self):
        self.assertEqual('Error', self.s.fun(1.1, 3.1, 0), 'good')

    def test_frak(self):
        self.assertEqual('Error', self.s.fun(1, 3.1, 0), 'good')

# 1 В отрицательное число
# 2 оба числа отрицательные
# 3 оба числа положительные
# 4  А>B
# 5  А = В
# 6  А число а В - буква
# 7  оба числа дробные
# 8 одно из чисел дробное, а второе целое
