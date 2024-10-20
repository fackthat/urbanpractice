import threading
from time import sleep, time
from datetime import datetime

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

time_start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = datetime.now()
print(f'Работа потоков {time_end - time_start}')

time_start_threads = time()

threads = [
       threading.Thread(target=write_words, args=(10, 'example5.txt')),
       threading.Thread(target=write_words, args=(30, 'example6.txt')),
       threading.Thread(target=write_words, args=(200, 'example7.txt')),
       threading.Thread(target=write_words, args=(100, 'example8.txt'))
]

for thread in threads:
    thread.start()

for thread in threads:
    (thread.join())

time_end_threads = time()
print(f'Работа потоков {time_end_threads - time_start_threads}')
