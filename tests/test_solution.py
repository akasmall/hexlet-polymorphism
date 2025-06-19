from solution import stringify
from faker import Faker


def test_stringify1():
    tag = {
        'name': 'hr',
        'class': 'px-3',
        'id': 'myid',
        'tag_type': 'single',
    }
    html = stringify(tag)

    expected = '<hr class="px-3" id="myid">'
    assert html == expected


def test_stringify2():
    tag = {
        'name': 'p',
        'tag_type': 'pair',
        'body': 'text',
    }
    html = stringify(tag)

    expected = '<p>text</p>'
    assert html == expected


def test_stringify3():
    tag = {
        'name': 'div',
        'tag_type': 'pair',
        'body': 'text2',
        'id': 'wow',
    }
    html = stringify(tag)
    expected = '<div id="wow">text2</div>'
    assert html == expected


def test_stringify4():
    fake = Faker()
    random_attr = fake.word()
    tag = {
        'name': 'div',
        'tag_type': 'pair',
        'body': 'text2',
        'id': 'wow',
        random_attr: 'value',
    }
    html = stringify(tag)

    expected = f'<div id="wow" {random_attr}="value">text2</div>'
    assert html == expected
