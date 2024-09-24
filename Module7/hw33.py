team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time)/tasks_total
challenge_result = team2_name

def challenge_result():
    if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
        result = 'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
        result = 'Победа команды Волшебники Данных!'
    else:
        result = 'Ничья!'
    return result


# Использование %
print('В команде %(name)s участников: %(participant)s!' % {'name': team1_name, 'participant': team1_num})
print('Итого сегодня в командах участников: %(p1)s и %(p2)s!' % {'p1': team1_num, 'p2': team2_num})

# Использование format()
print('Команда {name} решила задач: {score}!'.format(name=team2_name, score=score_1))
print('{name} решили задачи за {time} с!'.format(name=team2_name, time=team2_time))

# Использование f-строк
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result()}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!')