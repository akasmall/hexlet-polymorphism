### <span style="color:green">Создайте полноценное консольное приложение, которое показывает текущую погоду в городе.</span>
Оно работает так:
```bash
$ python scripts/weather.py berlin
Temperature in berlin: 11C // C - Цельсий

$ python scripts/weather.py monaco
Temperature in monaco: 26C
```
Это консольное приложение обращается внутри себя к сервису погоды. Сервис погоды расположен по адресу <span style="color:red">http ://localhost:8080</span> внутри практики. Информацию по городу можно извлечь, сделав **GET-запрос** на **URL-адрес** <span style="color:red">/api/v2/cities/<имя города></span>.

Данные от сервиса возвращаются в виде json: <span style="color:red">{ "name": "<имя города>", temperature: "<температура>" }</span>, единица измерения не указана, но это всегда градус Цельсия. Пример:

### <span style="color:green">Вы можете попробовать выполнить этот запрос прямо в терминале</span>
```bash
$ telnet localhost 8080
GET /api/v2/cities/berlin HTTP/1.1
HOST: localhost

HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: 41

"{\"name\":\"berlin\",\"temperature\":9}"
```

### <span style="color:red">weather_service.py</span>

Реализуйте логику работы сервиса <span style="color:red">WeatherService</span>. Под сервисом здесь понимается класс, умеющий работать с конкретным сервисом погоды (в интернете их довольно много). В перспективе классов может быть много и они могут подменять друг друга (то есть обеспечивать полиморфизм).

Объект этого класса должен уметь запрашивать данные у сервера с помощью метода <span style="color:red">look_up()</span> (по урлу выше) по конкретному городу и возвращать их обратно.
```
ws = WeatherService(http_client)
response = ws.look_up('Moscow')
print(response)  # {"name":"Moscow","temperature":21}
```
Для извлечения данных о погоде, ему нужно выполнить **http-запрос**. Для выполнения подобных запросов понадобится **http-клиент**, библиотека, которая сама формирует правильный **http-запрос** и возвращает ответ. В нашем случае используется <span style="color:red">requests</span>.

Сделайте так, чтобы **http-клиент** не был зашит внутри класса, используйте инъекцию зависимостей для проброса клиента внутрь. Потенциально это позволит подменить реализацию **http-клиента** (то есть использовать другой клиент), без необходимости переписывать код сервиса.

Пример того, как делаются запросы с помощью <span style="color:red">requests</span>:
```
## Выполнение GET запроса по указанному адресу
response = requests.get('https://hexlet.io/lessons?page=2')
## response содержит http-ответ
```
Структуру ответа можно посмотреть [здесь](https://requests.readthedocs.io/en/latest/user/quickstart/#response-content).

### <span style="color:red">scripts/weather.py</span>
Реализуйте код, вызывающий сервис и возвращающий ожидаемую строку. Аргументы командной строки передаются в вызове функции <span style="color:red">main()</span>. Все что вам нужно, лишь вызвать необходимый метод вашего сервиса и вернуть строку как в примере ниже

```
python scripts/weather.py monaco
Temperature in monaco: 23C
```
<span style="color:green">Подсказки</span>

[Скрипты](https://ru.hexlet.io/blog/posts/skripty-moduli-i-biblioteki), [модули](https://ru.hexlet.io/blog/posts/skripty-moduli-i-biblioteki) и [библиотеки](https://ru.hexlet.io/blog/posts/skripty-moduli-i-biblioteki)
