from fake_subscription import FakeSubscription


class User():
    def __init__(self, email, current_subscription=None):
        self.email = email
        # BEGIN (write your solution here)
        # self.current_subscription = current_subscription \
        #     if current_subscription is not None else FakeSubscription(
        #         self
        #     )
        if current_subscription is not None:
            self.current_subscription = current_subscription
        else:
            self.current_subscription = FakeSubscription(
                self
            )
        # END

    def get_current_subscription(self):
        return self.current_subscription

    def is_admin(self):
        return self.email == 'rakhim@hexlet.io'
