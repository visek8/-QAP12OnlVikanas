from pytest import fixture, mark


def space(x):
    try:
        return x.strip()
    except:
        return 0


@fixture()
def set_up():
    print('Start test')


class TestSpace:
    @mark.parametrize('a,r', (['привет мир!   ', 'привет мир!'],
                              ['    привет мир!', 'привет мир!'],
                              ['    привет мир!    ', 'привет мир!'],
                              ['          привет мир!          ', 'привет мир!'],
                              ['   привет мир!   ', 'привет мир!'],))
    def test_one(self, a, r):
        resalt = space(a)
        assert resalt == r
