import threading
import random
from time import sleep

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            amount = random.randint(50, 500)
            with self.lock:
                self.balance += amount
                print(f'Пополнение: {amount}. Баланс: {self.balance}')
                # if self.balance >= 500 and self.lock.locked():
                #     self.lock.release()
            sleep(0.001)

    def take(self):
        for i in range(100):
            amount = random.randint(50, 500)
            print(f'Запрос на {amount}')
            with self.lock:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f'Снятие: {amount}. Баланс: {self.balance}')
                else:
                    print(f'Запрос отклонён, недостаточно средств')
                    # self.lock.acquire()
            sleep(0.001)


bk = Bank()

t1 = threading.Thread(target=Bank.deposit, args=(bk,))
t2 = threading.Thread(target=Bank.take, args=(bk,))

t1.start()
t2.start()

t1.join()
t2.join()

print(f'Итоговый баланс: {bk.balance}')


