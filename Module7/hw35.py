

def add_everything_up(a, b):
    try:
        if (isinstance(a, (int, float))) and (isinstance(b, (int, float))):
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            return a + b
        else:
            return str(a) + str(b)
    except typeError as exc:
        print(f'Ошибка типа: {exc}', exc)
    except Exception as e:
        print(f'Ошибка: {e}')

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))