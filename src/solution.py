
# ?BEGIN (write your solution here)
def greet(obj):
    if obj.is_user():
        return f"Hello {obj.get_name()}!"
    else:
        return "Nice to meet you Guest!"
# ?END


# !решение ментора
# ?BEGIN
# \\MAPPING = {
# \\    'guest': lambda guest: f'Nice to meet you {guest.get_name()}!',
# \\    'user': lambda user: f'Hello {user.get_name()}!',
# \\}


# \\def greet(some_user):
# \\    return MAPPING[some_user.get_type()](some_user)
# ?END
