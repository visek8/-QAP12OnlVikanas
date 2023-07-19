from pytest import fixture, mark


def prod(n):
    if type(n) == int and n > 0 and n < 100:
        f = 1
        while n > 1:
            f *= n
            n -= 1
        return f
    else:
        return 'Error'


@fixture()
def set_up():
    print('Start test')


class TestMultiplication:
    @mark.parametrize('a,r', ([-4, 'Error'],
                              [0, 'Error'],
                              [0.5, 'Error'],
                              [2.5, 'Error'],
                              [4, 24],
                              ['!', 'Error'],
                              [+4, 24],
                              [1000000000, 'Error']))
    def test_one(self, a, r):
        resalt = prod(a)
        assert resalt == r
