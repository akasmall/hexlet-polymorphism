solution.py
Реализуйте функцию <span style="color:red">greet()</span>, которая возвращает приветствие для пользователя. Это приветствие показывается пользователю на сайте. Если пользователь <span style="color:green">гость</span>, то выводится <span style="color:green">"Nice to meet you Guest!"</span>, если не гость, то <span style="color:green">"Hello <Имя>!"</span>, где <span style="color:green">"<Имя>"</span> это имя реального пользователя. В этой задаче, способ решения остается на ваше усмотрение. Используйте знания полученные в этом курсе.

user.py
Допишите необходимые методы в классе <span style="color:red">User()</span>

guest.py
Допишите необходимые методы в классе <span style="color:red">Guest()</span>

```python
from guest import Guest
from user import User
from solution import greet

guest = Guest()
greet(guest)  # 'Nice to meet you Guest!'

user = User('Tota')
greet(user)  # 'Hello Tota!'
```

#### <span style="color:blue">Подсказки</span>
Изучите тесты

<span style="background-color: yellow; color: black">Выделенный текст</span>
