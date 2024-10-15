def is_prime_number(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_prime(func):
    def wrapper(a, b ,c):
        result = func(a, b, c)
        if is_prime_number(result):
            print("Простое")
        else:
            print("Составное")
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)