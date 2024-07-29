my_dict = {'Anton': 1990, 'Egor': 1991, 'Pavel': 1992}
print('Dictionary:', my_dict)
print('Found value:', my_dict['Anton'])
print(my_dict.get('Ekaterina', 'Error: There is not such identifier'))
my_dict.update({'Valeriya': 1993,
                'Eva': 1994})
a = my_dict.pop('Egor')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)
print('')
my_set = {1, 1, 2, 3, 3, 'String1', 'String2', 'String1', (1, 2, 3), (2, 3, 4), (1, 2, 3)}
print('Set:', my_set)
my_set.add(7)
my_set.add('String3')
my_set.discard((1, 2, 3))
print('Modified set:', my_set)