class User:
    def __init__(self, name):
        self.name = name
        # BEGIN (write your solution here)
        self._is_user = True
        # END

    def get_name(self):
        return self.name

    # BEGIN (write your solution here)
    def is_user(self):
        return True
    # END

# !решение ментора
# \\class User:
# \\    def __init__(self, name):
# \\        self.name = name
#         # BEGIN
# \\        self.type = 'user'
#         # END

# \\    def get_name(self):
# \\        return self.name

#     # BEGIN
# \\    def get_type(self):
# \\        return self.type
#     # END
