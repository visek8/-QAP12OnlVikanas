from pytest import fixture, mark


def fun(a, b, s):
    if type(a) == int and type(b) == int and type(s) == int:
        for i in range(a, b + 1):
            s = s + i
        return s
    else:
        return 'Error'


@fixture()
def set_up():
    print('Start test')


class TestSum:
    @mark.parametrize('a,b,s,r', ([1, -3, 0, 0],
                                  [-1, -3, 0, 0],
                                  [1, 3, 0, 6],
                                  [3, 1, 0, 0],
                                  [1, 1, 0, 1],
                                  [1, 'a', 0, 'Error'],
                                  [1.1, 3.1, 0, 'Error'],
                                  [1, 3.1, 0, 'Error']))
    def test_one(self, a, b, s, r):
        resalt = fun(a, b, s)
        assert resalt == r
