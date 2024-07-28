immutable_var = 1, 2, 'string', True
print(immutable_var)
# immutable_var[0] = 50
# print(immutable_var)
# Кортеж является неизменяемой коллекцией, поэтому изменить значения элементов кортежа нельзя
mutable_list = ['string1', 'string2', 1, 2, True]
print(mutable_list)
mutable_list.append('string3')
print(mutable_list)
mutable_list.extend(['string4', 3])
print(mutable_list)
mutable_list.remove(3)
print(mutable_list)
