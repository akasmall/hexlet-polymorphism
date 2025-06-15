from solution import get_links


def test_get_links_empty():
    tags = []
    links = get_links(tags)

    assert links == []


def test_get_links1():
    tags = [
        {'name': 'p'},
        {'name': 'a', 'href': 'hexlet.io'},
        {'name': 'img', 'src': 'hexlet.io/assets/logo.png'},
    ]

    links = get_links(tags)
    expected = [
        'hexlet.io',
        'hexlet.io/assets/logo.png',
    ]

    assert links == expected


def test_get_links2():
    tags = [
        {'name': 'img', 'src': 'hexlet.io/assets/logo.png'},
        {'name': 'div'},
        {'name': 'link', 'href': 'hexlet.io/assets/style.css'},
        {'name': 'h1'},
    ]
    links = get_links(tags)

    expected = [
        'hexlet.io/assets/logo.png',
        'hexlet.io/assets/style.css',
    ]
    assert links == expected


def test_get_links3():
    tags = [
        {'name': 'invalidTag', 'src': 'hexlet.io/assets/invalid.png'},
        {'name': 'img', 'src': 'hexlet.io/assets/logo.png'},
        {'name': 'div'},
        {'name': 'link', 'href': 'hexlet.io/assets/style.css'},
        {'name': 'h1'},
    ]
    links = get_links(tags)
    expected = [
        'hexlet.io/assets/logo.png',
        'hexlet.io/assets/style.css',
    ]
    assert links == expected
