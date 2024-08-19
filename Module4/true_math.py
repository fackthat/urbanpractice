from math import inf

def divide(first, second):
    if second == 0:
        return inf
    else:
        return first / second

# result = divide(89, 0)
# print(result)