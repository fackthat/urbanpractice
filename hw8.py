first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second and second == third:
    print('Все', 3, 'числа равны')
elif first == second or second == third or first == third:
    print('Только', 2, 'числа равны')
elif first != second and second != third and first != third:
    print(0, 'чисел равны')