## Асинхронность: определения, работа, различия, применение.

- **Вакансии**:
  - **Циан**: Понимание принципов асинхронности.
  - **Бьюти Бот**: Опыт работы с асинхронными фреймворками (FastAPI, asyncio).
  - **7tech**: Понимание принципов асинхронного программирования.

### Определение
> Асинхронность, многопоточность, многопроцессорность - это три подхода к выполнению параллельных задач в программировании.

> Асинхронность - это способ выполнения задач, при котором выполнение одной задачи не блокирует выполнение других. Это достигается за счет использования неблокирующих операций и событийного цикла.

### Работа 
В асинхронном программированию используются конструкции, такие как async и await, которые и позволяют писать код, который выглядит синхронно, но выполняется асинхронно.

Когда программа достигает операции ввода-вывода (например, запрос к базе данных или API), она может "отпустить" управление, позволяя другим задачам выполняться в это время.

### Применение 
Асихронность особенно полезна в веб-приложениях, где необходимо обрабатывать множество запросов одновременно, не блокируя сервер.

Из моей практики простые примеры: 
- [Модуль для работы с базой данных и сессиями SQLAlchemy](https://github.com/mikey-semy/work-aedb/blob/main/app/database/session.py)

В классе контекстного менеджера `SessionContextManager` для управления сессиями базы данных имеются асинхронные магические методы входа `__aenter__` и выхода `__aexit__`, методы фиксации изменений `commit` и откатывания изменений `rollback`. 

В `commit` и `rollback` имеются три await: 
- `commit()` - ожидает, пока изменения запишутся в базу;
- `rollback()` - ожидает, пока откатяться изменения;
- `close()` - ждет пока закроется сессия.

<details>
<summary>session.py</summary>

```python
class SessionContextManager():
    """
    Контекстный менеджер для управления сессиями базы данных.
    """

    def __init__(self) -> None:
        """
        Инициализирует экземпляр SessionContextManager.
        """
        self.db_session = DatabaseSession(config)
        self.session_factory = self.db_session.create_async_session_factory()
        self.session = None

    async def __aenter__(self) -> 'SessionContextManager':
        """
        Асинхронный метод входа в контекстный менеджер.

        Returns:
            SessionContextManager: Экземпляр текущего контекстного менеджера.
        """
        self.session = self.session_factory()
        return self

    async def __aexit__(self, *args: object) -> None:
        """
        Асинхронный метод выхода из контекстного менеджера.

        Args:
            *args: Аргументы, передаваемые при выходе из контекста.
        """
        await self.rollback()

    async def commit(self) -> None:
        """
        Асинхронно фиксирует изменения в базе данных и закрывает сессию.
        """
        await self.session.commit()
        await self.session.close()
        self.session = None

    async def rollback(self) -> None:
        """
        Асинхронно откатывает изменения в базе данных и закрывает сессию.
        """
        await self.session.rollback()
        await self.session.close()
        self.session = None
```

</details>

- [Основной модуль маршрутизации для главной страницы](https://github.com/mikey-semy/work-aedb/blob/main/app/routers/v1/main.py)

Асинхронная функция `homepage` без await, так как `TemplateResponse` не выполняет никаких IO операций в момент создания - он просто создает объект ответа. А async нужен для совместимости с остальной асинхронной инфраструктурой:
- Поддержание асинхронный pipeline FastAPI;
- Возможность добавить асинхронные операции в будущем (например, обращение к БД);
- Не блокировать event loop, позволяя обрабатывать другие запросы параллельно.

<details>
<summary>main.py</summary>

```python
"""
Основной модуль маршрутизации для приложения AEDB.

Этот модуль определяет маршруты для главной страницы. 
Он использует шаблоны Jinja2 для рендеринга HTML-ответов.

Маршруты:
- /: Главная страница

Каждый маршрут возвращает HTML-ответ, используя соответствующий шаблон.
"""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.const import main_params, templates_path

templates = Jinja2Templates(directory=str(templates_path))

router = APIRouter(**main_params)

@router.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    """
    Обрабатывает запросы к главной странице.

    Args:
        request (Request): Объект запроса FastAPI.

    Returns:
        TemplateResponse: Отрендеренный HTML-ответ для главной страницы.
    """
    context = {
        "title": "AEDB",
        }
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context=context
    )
```

</details>