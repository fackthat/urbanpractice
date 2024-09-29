
def person_sum(numbers):
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            if isinstance(number, (int, float)):
                result += number
            else:
                raise ValueError
        except (TypeError, ValueError):
            print(f'Некорректный тип данных для подсчёта суммы - {number}')
            incorrect_data += 1
    return result, incorrect_data

def calculate_average(numbers):
    try:
        if isinstance(numbers, str):
            numbers = list(numbers)
        if isinstance(numbers, (list, tuple, set)):
            total_sum, incorrect_count = person_sum(numbers)
            correct_count = len(numbers) - incorrect_count
            if correct_count == 0:
                return 0
            else:
                return total_sum / correct_count
        else:
            print(f'В numbers записан некорректный тип данных')
            return None
    except ZeroDivisionError:
        return 0


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

        







