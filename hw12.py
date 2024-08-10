import random
n = random.randint(3, 20)
print('Первое число:', n)
password = []
for i in range(1, 21):
    for j in range(2, 21):
        if i >= j:
            continue
        else:
            count = n % (i + j)
            if count != 0:
                continue
            else:
                password.extend([str(i), str(j)])
result = ''.join(password)
print('Второе число:', result)


