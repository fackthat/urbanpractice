from threading import Thread
from time import sleep
from random import randint
from queue import Queue

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        wait = randint(3, 10)
        sleep(wait)

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        for guest in guests:
            free_table = next((table for table in self.tables if table.guest is None), None)
            if free_table is not None:  # Если есть свободный стол
                free_table.guest = guest  # Сажаем гостя за стол
                guest.start()  # Запускаем поток гостя (процесс питания)
                print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
            else:  # Если свободных столов нет, гость попадает в очередь
                self.queue.put(guest)
                print(f"{guest.name} в очереди")


    def discuss_guests(self):
        # Продолжаем, пока очередь не пуста или хотя бы один стол занят
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():  # Гость покушал и ушёл
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None  # Освобождаем стол
                    # Проверяем, есть ли гости в очереди
                    if not self.queue.empty():
                        next_guest = self.queue.get()  # Берем следующего гостя из очереди
                        table.guest = next_guest  # Сажаем его за освободившийся стол
                        next_guest.start()  # Запускаем поток гостя
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
            sleep(1)  # Проверяем состояние каждые 1 секунду





# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()