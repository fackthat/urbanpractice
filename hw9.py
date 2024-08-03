my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = len(my_list)
count = 0
while 0 < a:
    num = my_list[count]
    count = count + 1
    if num < 0 or count == a:
        break
    elif num == 0:
        continue
    print(num)
