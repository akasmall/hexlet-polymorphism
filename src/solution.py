# ?BEGIN (write your solution here)
# from in_memory_kv import InMemoryKV


def swap_key_value(obj):
    obj.new_dist = dict(zip(obj.new_dist.values(), obj.new_dist.keys()))


# map = InMemoryKV({'key': 10})
# print(map.get_('key'))
# map.set_('key2', 'value2')
# print(map.get_('key2'))
# print(swap_key_value(map))


# ?END


# !решение ментора
# BEGIN
# \\def swap_key_value(map):
# \\    data = map.to_dict()
# \\    for key in data:
# \\        map.unset_(key)

# \\    for key, value in data.items():
# \\        map.set_(value, key)
# END
