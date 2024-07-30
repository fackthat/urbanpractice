grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
dictionary = {}
pupils = list(students)
pupils.sort()
dictionary.update({pupils[0]:sum(grades[0])/len(grades[0]),
                   pupils[1]:sum(grades[1])/len(grades[1]),
                   pupils[2]:sum(grades[2])/len(grades[2]),
                   pupils[3]:sum(grades[3])/len(grades[3]),
                   pupils[4]:sum(grades[4])/len(grades[4])})
print('Средние баллы учеников:', dictionary)
view = input('Введите имя ученика: ')
if pupils[0] == view:
    print(sum(grades[0]) / len(grades[0]))
    if pupils[1] == view:
        print(sum(grades[1]) / len(grades[1]))
        if pupils[2] == view:
            print(sum(grades[2]) / len(grades[2]))
            if pupils[3] == view:
                print(sum(grades[3]) / len(grades[3]))
                if pupils[4] == view:
                    print(sum(grades[4]) / len(grades[4]))
