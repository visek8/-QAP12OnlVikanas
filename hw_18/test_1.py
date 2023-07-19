import unittest


class Space:
    def space(self, x):
        try:
            return x.strip()
        except:
            return 0


class TestSpace(unittest.TestCase):
    def setUp(self) -> None:
        self.sp = Space()

    def test_head(self):
        self.assertEqual('привет мир!', self.sp.space('привет мир!    '), 'good')

    def test_tail(self):
        self.assertEqual('привет мир!', self.sp.space('    привет мир!'), 'good')

    def test_parity(self):
        self.assertEqual('привет мир!', self.sp.space('    привет мир!    '), 'good')

    def test_ten(self):
        self.assertEqual('привет мир!', self.sp.space('          привет мир!          '), 'good')

    def test_noparity(self):
        self.assertEqual('привет мир!', self.sp.space('   привет мир!   '), 'good')

# 1 отсутствии проблеов только в начале
# 2 отстутсвии пробелов только в конце
# 3 наличии четного количества пробелов
# 4 наличии 10 пробелов
# 5 наличии нечетного количества пробелов
