def add(x, y=2):
    return x + y

def product(x, y=2):
    return x * y


def test_add():
    assert add(4, 3) == 7
    assert add(5) != 5


def test_product():
    assert product(4, 3) == 7
    assert product(3) == 6


def test_addString():
    result = add('Hello', ' Bolo')
    assert result == 'Hello Bolo'
    assert type(result) is str
    assert 'Hell' not in result


def test_productString():
    assert product('Hello', 3) == 'HelloHelloHello'
    result = product('Hell')
    assert result == 'HellHell'
    assert type(result) is str