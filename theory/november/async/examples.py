from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import gc
import json
import time

def work(size):
    json.dumps(list(range(size)))

def sequential(size, count):
    for _ in range(count):
        work(size)

def run_threads(size, count):
    with ThreadPoolExecutor() as executor:
        executor.map(work, [size] * count)

def run_processes(size, count):
    with ProcessPoolExecutor() as executor:
        executor.map(work, [size] * count)

if __name__ == '__main__':
    # gc.disable()

    size = 1000000
    testCases = [ (size,  i) for i in range(1, 12)]
    variants = [sequential, run_threads, run_processes]

    for i, t in enumerate(testCases):
        size, executionUnitsCount = t
        print(f"Parallelism: {executionUnitsCount}, JSON Size: {size}")
        
        for j, variant in enumerate(variants):        
            start = time.perf_counter()

            variant(size, executionUnitsCount)

            end = time.perf_counter()

            print(f"{variant.__name__}, elapsed: {round(end - start, 2)}")
        print()


# Идеи для практики
# Скачивание файлов: Написать программу, которая загружает несколько файлов из интернета параллельно. Использовать asyncio для асинхронного скачивания, чтобы не блокировать выполнение программы.
# Обработка изображений: Создать скрипт, который обрабатывает (например, изменяет размер или применяет фильтры) множество изображений в папке. Использовать multiprocessing для распараллеливания обработки изображений, чтобы ускорить выполнение.
# Парсинг веб-страниц: Разработать веб-скрейпер, который собирает данные с нескольких веб-сайтов одновременно. Использовать threading или asyncio для асинхронного выполнения запросов к сайтам.
# Чтение и запись в базу данных: Написать программу, которая одновременно читает данные из одной таблицы базы данных и записывает их в другую. Использовать multiprocessing для параллельной обработки данных.
# Обработка логов: Создать систему, которая анализирует логи сервера в реальном времени, фильтруя и обрабатывая записи. Использовать asyncio для асинхронного чтения логов и обработки данных.
# Криптографические вычисления: Разработать программу для параллельного вычисления хешей (например, SHA-256) для большого количества файлов. Использовать multiprocessing для распределения нагрузки между процессами.
# Обработка данных из API: Написать скрипт, который запрашивает данные из нескольких API и обрабатывает их. Использовать asyncio для асинхронных запросов и обработки ответов.
# Тестирование производительности: Создать инструмент для тестирования производительности веб-сервиса, который отправляет множество запросов одновременно. Использовать threading или asyncio для имитации нагрузки.
# Синхронизация данных: Разработать программу, которая синхронизирует данные между двумя источниками (например, локальной базой данных и облачным хранилищем) с использованием параллельных потоков для повышения скорости.
# Обработка видео: Написать скрипт, который разбивает видео на кадры и обрабатывает каждый кадр (например, применяет фильтры или распознает объекты). Использовать multiprocessing для распараллеливания обработки кадров.
# Напишите программу, которая одновременно загружает несколько веб-страниц и сохраняет их содержимое в файлы.
# Создайте программу, которая использует многопоточность для чтения и записи данных в базу данных.
# Напишите программу, которая одновременно выполняет несколько задач CPU-интенсивных вычислений, таких как вычисление факториала числа или сортировка списка.
# Создайте программу, которая использует многопроцессорность для обработки изображений, таких как изменение размера или применения фильтров.
# Напишите программу, которая одновременно загружает несколько файлов из сети и сохраняет их на диске.
# Создайте программу, которая использует асинхронный параллелизм для отправки и получения данных по сети, используя протоколы HTTP или TCP.
# Напишите программу, которая одновременно выполняет несколько задач, требующих доступа к диску, таких как чтение и запись файлов или баз данных.
# Создайте программу, которая использует многопоточность для выполнения задач, требующих доступа к сети, таких как отправка и получение данных по HTTP или TCP.
# Напишите программу, которая одновременно выполняет несколько задач, требующих доступа к базе данных, таких как чтение и запись данных или выполнение запросов.
# Создайте программу, которая использует многопроцессорность для выполнения задач, требующих доступа к ресурсам системы, таким как CPU, память или дисковое пространство.