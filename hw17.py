def get_multiplied_digits(number):
    number = int(number)
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


num = input('Введите целое число: ')
print(f'Произведение цифр числа {num} :', get_multiplied_digits(num))


# result = get_multiplied_digits(00123)
# print(result)