# BEGIN (write your solution here)
class FakeSubscription():
    def __init__(self, user):
        self.user = user

    def has_professional_access(self):
        return self.user.is_admin()

    def has_premium_access(self):
        return self.user.is_admin()
# END
