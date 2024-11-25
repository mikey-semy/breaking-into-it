## Асинхронность, многопоточность, многопроцесcность: определения, работа, различия, применение.
> Асинхронность, многопоточность, многопроцесcность - это три подхода к выполнению параллельных задач в программировании.

- **Вакансии**:
  - **Циан**: Понимание принципов асинхронности.
  - **Бьюти Бот**: Опыт работы с асинхронными фреймворками (FastAPI, asyncio).
  - **7tech**: Понимание принципов асинхронного программирования.

# Асинхронность (asyncio)
### Определение


> Асинхронность - это способ выполнения операций, при котором выполнение задачи не блокирует основной поток выполнения программы. Вместо этого программа может продолжать выполнять другие задачи, пока ожидает завершения асинхронной операции.

### Работа 
В асинхронном программированию используются конструкции, такие как async и await, которые и позволяют писать код, который выглядит синхронно, но выполняется асинхронно.

Когда программа достигает операции ввода-вывода (например, запрос к базе данных или API), она может "отпустить" управление, позволяя другим задачам выполняться в это время.

### Применение 
Асихронность особенно полезна в веб-приложениях, где необходимо обрабатывать множество запросов одновременно, не блокируя сервер.

Или вот примеры применения:
- Сетевые запросы: Если ваша программа выполняет HTTP-запросы (например, к API или веб-сайтам), эти операции обычно занимают время из-за задержек сети. Их следует делать асинхронными, чтобы не блокировать выполнение программы, пока ожидается ответ. (aiohttp)
- Ввод-вывод (I/O): Операции, связанные с чтением и записью файлов, базами данных и другими внешними ресурсами, также могут быть асинхронными. Это позволяет программе продолжать выполнение других задач, пока ожидается завершение операции ввода-вывода. (aiofiles, sqlalchemy.ext.asyncio)
- Долгие вычисления: Если у вас есть операции, которые требуют значительных вычислительных ресурсов и могут занять много времени, их лучше выполнять в отдельных потоках или процессах, чтобы не блокировать основной поток выполнения. (asyncio)

### Почитать
- [Асинхронный python без головной боли (часть 1)](https://habr.com/ru/articles/667630/)
- [Асинхронный python без головной боли (часть 2)](https://habr.com/ru/articles/671798/)
- [Асинхронный python без головной боли (часть 3)](https://habr.com/ru/articles/774582/)


# Многопроцессность (multiprocessing)
### Определение
— это способ выполнения нескольких процессов одновременно. Каждый процесс имеет свою собственную память и ресурсы, что делает их более изолированными друг от друга по сравнению с потоками.
### Работа
Многопроцессность реализуется с помощью создания отдельных процессов, которые могут взаимодействовать друг с другом через механизмы межпроцессного взаимодействия (IPC), такие как очереди сообщений, сокеты или общая память.
### Применение 
Многопроцессность часто используется в приложениях, требующих высокой надежности и изоляции, таких как серверные приложения, обработка больших данных и системы, где сбой одного процесса не должен влиять на другие.

# Многопоточность (threading)
### Определение
— это возможность выполнения нескольких потоков (легковесных процессов) в рамках одного процесса. Каждый поток может выполнять свою задачу, и они могут работать параллельно, используя общую память.
### Работа
Потоки могут быть созданы и управляемы с помощью библиотек и фреймворков, таких как threading в Python или java.lang.Thread в Java.
Многопоточность позволяет эффективно использовать многоядерные процессоры.
### Применение 
Многопоточность полезна в приложениях, требующих высокой производительности, таких как серверы, игры и приложения с интенсивными вычислениями, где задачи могут выполняться параллельно.

# Различия

Если асинхронность - это конкурентные потоки, которые не выполняются параллельно. 
То многопроцессность (multiprocessing) - это когда каждый процесс имеет свою область памяти, отдельный интерпретатор Python со своим GIL и с соответствующими расходами ресурсов.
А многопоточность (threading) - все потоки используют общую память.

Таким образом, основные различия следующие: 
- Изоляция: Процессы изолированы друг от друга, в то время как потоки разделяют память. Асинхронные операции не требуют создания новых потоков или процессов.
- Нагрузка на ресурсы: Многопоточность и многопроцессность требуют больше ресурсов, чем асинхронность, так как создаются дополнительные потоки или процессы.
- Сложность: Многопоточность и многопроцессность могут быть сложнее в реализации из-за необходимости управления состоянием и синхронизацией, в то время как асинхронность часто проще в использовании.

### Почитать
- [Различные вычисления, многопоточность, асинхронность и мультипроцессность в Python](https://habr.com/ru/companies/sberbank/articles/829098/)


### Пройти
- [Многопоточность и многопроцессорность Python](https://stepik.org/lesson/628334/step/1?unit=624214)


## Хоть какая-то практика
#### 1. Асинхронный модуль для скрапинга сайтов:

Разработать асинхронный [модуль для скрапинга сайтов](https://github.com/mikey-semy/apartment-serbia-telegrambot/blob/master/app/modules/WebScraper.py), который позволит эффективно извлекать данные. Это может быть полезно для получения информации о недвижимости, как в текущем проекте Apartment Serbia Telegram Bot.

В дальнейшем, на основе этого модуля, создать функционал для скрапинга ссылок [радио](https://radiopotok.ru/), который будет использоваться для создания плеера в проекте AEDB. Этот плеер можно будет интегрировать в качестве виджета на главной странице.


### Реализация 
#### 1. [Асинхронный модуль для скрапинга сайтов](https://github.com/mikey-semy/apartment-serbia-telegrambot/blob/master/app/modules/AsyncWebScraper.py):

1. Переписаная функция get_page:

```python
    async def aget_page(self, url) -> object:
        '''Асинхронная функция отправляет GET-запрос к URL и возвращает объект BeautifulSoup'''
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url, 
                headers=Config.WebScraper.HEADERS, 
                timeout=Config.WebScraper.TIMEOUT) as response:
                html = await response.text()
                return BeautifulSoup(html, 'html.parser')
```
Заместо `requests` используется асинхронный `aiohttp`.

2. Также переписана функция задержки, предотвращающая блокировку скрейпера
```python
async def ascrape_pause(self, 
                     min_pause=Config.WebScraper.MIN_PAUSE, 
                     max_pause=Config.WebScraper.MAX_PAUSE) -> None:
        '''Асинхронная функция вводит задержку, чтобы предотвратить блокировку скрейпера'''
        delay = random.uniform(min_pause, max_pause)
        await asyncio.sleep(delay)
```
Используется `asyncio.sleep`.

3. И сама функция `ascrape_page` включает в себя await `self.ascrape_pause()`

4. Функция, которая измеряется с помощью [таймера](https://gist.github.com/mikey-semy/30d78d781d42cc5179ca5a654480f0ca)

```python
@timer
async def aget_data(self, urls: list, current_page_number: int = 1, quantity_pages: int = Config.WebScraper.QUANTITY_PAGE) -> list:
    '''Асинхронная функция get_data собирает данные со всех страниц сайта'''
       
    last_page_number = quantity_pages

    all_offers = []

    for url in urls:
        while True:

            scraper = self.__get_scraper(url, current_page_number)

            soup = await scraper.aget_page(url)

            offers_from_page = await scraper.ascrape_page(soup)

            for offer in offers_from_page:
                all_offers.append(offer)

            if not scraper.has_next_page(soup) or current_page_number == last_page_number:
                break

            current_page_number += 1

    return all_offers
```

Запрос выполняю по трем ссылкам: 

```python
url_ = [

"https://www.nekretnine.rs/apartmani/grad/beograd/kvadratura/1_500/cena/0_1000000",

"https://cityexpert.rs/izdavanje-nekretnina/beograd?ptId=1&maxPrice=550&polygonsArray=Novi%20Beograd",

"https://www.4zida.rs/prodaja-stanova/novi-sad/do-47000-evra?vece_od=25m2&manje_od=30m2&skuplje_od=45000eur"

]
```

Результаты тестов: 
| Тест | WebScraper | AsyncWebScraper |
|------|---------------------|---------------------|
| 1    | 17.51 секунды        | 1.19 секунды        |
| 2    | 16.22 секунды        | 7.15 секунды        |
| 3    | 16.39 секунды        | 9.53 секунды        |
| 4    | 16.30 секунды        | 7.15 секунды        |
| 5    | 15.72 секунды        | 7.15 секунды        |

Надеюсь, я правильно измеряю время, нужно опробывать с time.strftime('%X').
> Да, в коде много недостатоков: отсутствие обработки ошибок, проверок наличия элементов и пустых значений, логирования и пр.
