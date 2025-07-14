class Guest:
    def __init__(self):
        self.name = 'Guest'
        # BEGIN (write your solution here)
        self._is_user = False
        # END

    def get_name(self):
        return self.name

    # BEGIN (write your solution here)
    def is_user(self):
        return False
    # END

# !решение ментора
# \\class Guest:
# \\    def __init__(self):
# \\        self.name = 'Guest'
#         # BEGIN
# \\        self.type = 'guest'
#         # END

# \\    def get_name(self):
# \\        return self.name

#     # BEGIN
# \\    def get_type(self):
# \\        return self.type
#     # END
