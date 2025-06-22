import copy


# BEGIN (write your solution here)
class InMemoryKV():
    def __init__(self, key_value):
        self.new_dist = copy.copy(key_value)
        # self.new_dist = copy.deepcopy(key_value)

    def set_(self, key, value):
        self.new_dist[key] = value

    def unset_(self, key):
        self.new_dist.pop(key, None)

    def get_(self, key, default=None):
        return self.new_dist.get(key, default)

    def to_dict(self):
        return copy.deepcopy(self.new_dist)

# END


# !решение ментора
# BEGIN (write your solution here)

# \\class InMemoryKV():
# \\    def __init__(self, initial=None):
# \\        if initial is None:
# \\            self.map = {}
# \\        else:
# \\            self.map = copy.deepcopy(initial)

# \\    def set_(self, key, value):
# \\        self.map[key] = value

# \\    def unset_(self, key):
# \\        self.map.pop(key)

# \\    def get_(self, key, default=None):
# \\        return self.map.get(key, default)

# \\    def to_dict(self):
# \\        return copy.deepcopy(self.map)
# END
