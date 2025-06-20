import json


# ?BEGIN (write your solution here)
class DatabaseConfigLoader:
    def __init__(self, path):
        self.path = path

    def load(self, config_name, config_result=None):
        if config_result is None:
            # Инициализация словаря при первом вызове
            config_result = {}
        config = None
        filename = str(self.path) + f"/database.{config_name}.json"
        if filename is not None:
            with open(filename, "r") as fd:
                config = json.load(fd)
        else:
            raise Exception("Improperly configured")

        key_extend = None
        if config.get("extend"):  # Если есть ключ extend
            # Берем значение по этому ключу и удаляем
            key_extend = config.pop("extend")
            # Рекурсивный вызов с новым аргументом и текущим результатом
            self.load(key_extend, config)

        # Объединяем полученный словарь если он есть с общим результатом
        config_result.update(
            {
                key: config[key] for key in config
                if key not in config_result and key != key_extend
            }
        )
        return config_result
# ?END


# !решение ментора
# ?BEGIN (write your solution here)
# class DatabaseConfigLoader():
#     def __init__(self, path):
#         self.path_to_config = path

#     def load(self, env):
#         filename = f'database.{env}.json'
#         filepath = self.path_to_config / filename
#         raw_config = json.loads(open(filepath).read())

#         if 'extend' not in raw_config:
#             return raw_config

#         extend = raw_config['extend']
#         rest = {k: v for k, v in raw_config.items() if k != 'extend'}
#         return {**self.load(extend), **rest}   # для python 3.5 и выше
#         return self.load(extend) | rest   # для python 3.9 и выше
# ?END
