
# !src/solution.py
# ?Реализуйте класс DatabaseConfigLoader, который отвечает за загрузку
# конфигурации для базы данных.
# ?У класса следующий интерфейс:

# ?__init__()
# - принимает на вход путь, по которому нужно искать конфигурацию
# ?load(env)
# - метод, который грузит конфигурацию для конкретной
# среды окружения. Он загружает файл
# ?database.{env}.json,
# парсит его и возвращает результат наружу.

# \\path_to_configs = path.join(__dirname, '__fixtures__')
# \\loader = DatabaseConfigLoader(path_to_configs)
# \\config = loader.load('production')

# \\production.json
# \\# {
# \\# host: 'google.com',
# \\# username: 'postgres',
# \\# };

# В этом классе и конфигурации реализована поддержка расширения.
# Если в загружаемой конфигурации есть ключ extend, то нужно загрузить
# конфигурацию с именем, хранящимся в этом ключе.
# ?Например:

# \\{
# \\    "extend": "development",
# \\    "host": "dev.server",
# \\    "password": "admin"
# \\}

# ?В ключе extend хранится значение 'development', поэтому дополнительно
# загружается конфигурация database.development.json также далее с новой
# загруженной конфигурацией.

# Конфигурации сливаются между собой так, что приоритет имеет загруженная
# раньше. Итоговая конфигурация не должна содержать ключ extend. Подробнее
# смотрите примеры в тестах.

# ?Подсказки
# путь передается Path объектом
