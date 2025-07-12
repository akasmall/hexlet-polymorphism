
# # ?На Хекслете доступ к курсам оформляется через подписку.
# ?Подписка
# — это отдельная сущность, которая хранит в себе информацию о самой
# подписке: когда она началась, сколько продолжается, оплачена ли и так далее.
# Типичная проверка на наличие подписки (а значит доступ к платному контенту)
# выглядит так:

# ?# Эти примеры сильно упрощены, к тому же Хекслет написан на Rails
# ?# но для демонстрации идеи такая реализация подойдет
# \\from user import User
# \\from subscription import Subscription
# \\user.get_current_subscription().has_premium_access()
# \\user.get_current_subscription().has_professional_access()
# Но не у всех пользователей есть подписка, на Хекслете есть и большая
# бесплатная часть.
# Так как подписка может отсутствовать, в коде придется делать так:

# \\if user.get_current_subscription()
# \\  and user.get_current_subscription().has_premium_access():
#    # есть премиум доступ, показываем что-то особенное

# Чтобы избежать постоянных проверок на существование подписки,
# мы внедрили Null Object. Теперь подписка есть всегда и достаточно написать:

# \\if user.get_current_subscription().has_professional_access():
#    # есть профессиональный доступ, показываем что-то особенное

# \\fake_subscription.py
# Реализуйте класс
# ?FakeSubscription
# FakeSubscription принимает пользователя. Если пользователь — администратор
# ?user.is_admin()
# , то все доступы разрешены, если нет — запрещены.
# Класс должен повторять интерфейс класса
# ?Subscription
# , то есть иметь те же методы, но со своей логикой.

# ?user.py
# Допишите
# ?__init__()
# пользователя, так, чтобы внутри устанавливалась реальная
# подписка если она передана снаружи и создавалась фейковая в ином случае.


# \\user1 = User('vasya@email.com', Subscription('premium'))
# \\user1.get_current_subscription().has_premium_access()
# # True
# \\user1.get_current_subscription().has_professional_access()
# # False

# \\user2 = User('vasya@email.com', Subscription('professional'))
# \\user2.get_current_subscription().has_premium_access()
# # False
# \\user2.get_current_subscription().has_professional_access()
# # True

# # Внутри создается фейковая, потому что подписка не передается
# \\user3 = User('vasya@email.com')
# \\user3.get_current_subscription().has_premium_access()
# # False
# \\user3.get_current_subscription().has_professional_access()
# # False

# \\user4 = User('rakhim@hexlet.io')
# # администратор, проверяется по емейлу
# \\user4.get_current_subscription().has_premium_access()
# # True
# \\user4.get_current_subscription().has_professional_access()
# # True
