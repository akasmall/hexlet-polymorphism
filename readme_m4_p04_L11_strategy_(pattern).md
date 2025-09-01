### <span style="color:green">Эта практика демонстрирует реализацию динамической диспетчеризации без использования классов.</span><br/>
Она больше рассчитана на изучение существующего кода, чем на написание нового. Разобравшись в ней, вы поймете что динамическая диспетчеризация может быть реализована практически в любом языке.

Когда речь идет не о полиморфном коде, то абстракции создаются как обычно используя конструкторы и селекторы:
```python
circle = Circle.make(5)
print(Circle.get_radius(circle)) # 5

square = Square.make(10)
print(Square.get_side(square)) # 10
```
Если функция должна быть полиморфной, то она создается через специальный (самописный) механизм. Этот механизм описан в файле <span style="color:green">dispatcher.py</span> и содержит некоторые запрещенные приемы (использование глобальной переменной), которые необходимы для реализации виртуальной таблицы. Будет здорово если вы разберетесь в устройстве этого кода.

В нашем случае добавляется ровно одна полиморфная функция <span style="color:green">get_area()</span>. Сначала посмотрим как этот код работает:

```python
import figure as Figure # Специальный модуль, который содержит полиморфную функцию
import circle as Circle
import square as Square
```

### Инициализация полиморфных методов
```bash
Circle.init()
Square.init()

circle = Circle.make(5)
square = Square.make(5)
```
### Вызов полиморфной функции.
В зависимости от типа она идет либо в circle либо в square
```bash
Figure.get_area(circle) # ~ 78.5
Figure.get_area(square) # 25
```
Теперь реализация. Первым делом создается специальный неймспейс с полиморфной функцией:
```python
from dispatcher import call

def get_area(self, *args):
    return call(self, get_area.__name__, args)
```
Он вызывает диспетчер, который, в свою очередь, выполняет поиск нужной реализации функции в виртуальной таблице и вызывает ее. Для работы диспетчера нужно чтобы любая абстракция была создана с помощью словаря, в котором под свойством name хранится тип сущности:

# src/circle.py
```python
def make(radius):
    return {'name': __name__, 'data': {'radius': radius}}
```
И последний шаг. Нужно создать реализацию функции именно для нашей текущей абстракции. Она делается в функции <span style="color:green">init</span>:
```python
from dispatcher import defmethod

def init():
    defmethod(__name__, 'get_area', lambda self: pi * self['data']['radius'] ** 2)
```
В этом месте происходит добавление функции конкретной абстракции circle в виртуальную таблицу

<span style="color:red">src/square.py</span><br/>
Реализуйте абстракцию <span style="color:green">square</span> опираясь на <span style="color:green">circle</span>. Эта абстракция должна содержать следующие функции:

- Конструктор, который принимает на вход длину стороны<br/>
- Селектор <span style="color:green">get_side</span>, который возвращает сторону<br/>
- Полиморфную функцию <span style="color:green">get_area</span>, которая возвращает площадь квадрата
```python
import figure as Figure # Специальный модуль, который содержит полиморфную функцию
import square as Square

Square.init()

square = Square.make(2)
Square.get_side(square) # 2
Figure.get_area(square) # 4
```
