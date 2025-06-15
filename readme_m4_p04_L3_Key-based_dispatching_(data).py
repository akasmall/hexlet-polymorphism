
# from solution import get_links
# src/solution.py
# Реализуйте функцию get_links(), которая принимает на вход список тегов,
# находит среди них теги a, link и img, а затем извлекает ссылки и возвращает
# список ссылок. Теги подаются на вход в виде списка, где каждый элемент
# это тег. Тег имеет следующую структуру:

# ?name — имя тега.
# ?href или src — атрибуты.
# ?Атрибуты зависят от тега:
# \\тег img имеет атрибут src,
# \\тег a — href, link — href.
# Примеры

# tags = [
#     {'name': 'img', 'src': 'hexlet.io/assets/logo.png'},
#     {'name': 'div'},
#     {'name': 'link', 'href': 'hexlet.io/assets/style.css'},
#     {'name': 'h1'},
# ]

# \\links = get_links(tags)
# \\# [
# \\# 'hexlet.io/assets/logo.png',
# \\# 'hexlet.io/assets/style.css'
# \\# ]
