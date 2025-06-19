
# !src/solution.py
# ?Реализуйте функцию stringify(), которая принимает на вход тег
# ?и возвращает его текстовое представление.

# \\from solution import stringify

# \\hr_tag = {
# \\    'name': 'hr',
# \\    'class': 'px-3',
# \\    'id': 'myid',
# \\    'tag_type': 'single',
# \\}
# \\html = stringify(hr_tag)  # <hr class="px-3" id="myid">

# \\div_tag = {
# \\    'name': 'div',
# \\    'tag_type': 'pair',
# \\    'body': 'text2',
# \\    'id': 'wow',
# \\}
# \\html = stringify(div_tag)  # <div id="wow">text2</div>

# \\empty_div_tag = {
# \\    'name': 'div',
# \\    'tag_type': 'pair',
# \\    'body': '',
# \\    'id': 'empty',
# \\}
# \\html = stringify(empty_div_tag)  # <div id="empty"></div>
# !Примечания
# ?В структуре тега есть три специальных ключа:

# ?name — имя тега
# ?tag_type — тип тега, определяет его парность(pair) или одиночность(single)
# ?body — тело тега, используется для парных тегов.
# Если у парного тега нет содержимого, то body равно пустой строке ''.
# Всё остальное становится атрибутами тега и не зависит от того,
# парный он или нет.

# ?Постарайтесь решить задание с помощью диспетчеризации по ключу.
