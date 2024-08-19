data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(*args):
  sum = 0
  if isinstance(args[0], (int, float)):
    sum += args[0]
  elif isinstance(args[0], (str)):
    sum += len(args[0])
  elif isinstance(args[0], (list, set, tuple)):
    for i in args[0]:
      sum += calculate_structure_sum(i)
  elif isinstance(args[0], (dict)):
    for key, value in args[0].items():
      sum += calculate_structure_sum(key)
      sum += calculate_structure_sum(value)
  return sum


result = calculate_structure_sum(data_structure)
print(result)
