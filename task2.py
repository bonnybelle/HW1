# 2. даны два словаря
# a = {'a': 1, 'b': 4, 't': 67}
# b = {'c': 4, 'e': 1, 'a': 4, 't': 7, 'y': 11}
#    2.1 найти ключи которые есть в обоих словарях
#    2.2 найти ключи которые есть только во 2м словаре, но нет в 1м
#    2.3 объединить словари в один, так чтоб числа при одинаковых ключах суммировались

dict1 = {'a': 1, 'b': 4, 't': 67}
dict2 = {'c': 4, 'e': 1, 'a': 4, 't': 7, 'y': 11}
dict3 = {}
lst1 = []
lst2 = []
for key, value in dict2.items():
    dict3[key] = value
    lst1.append(key) if key in dict1 else lst2.append(key)
for key, value in dict1.items():
    if key in dict3:
        dict3[key] += value
    else:
        dict3[key] = value
print('Общие ключи:', lst1, '\nТолько во 2м словаре:', lst2, '\nНовый словарь:', dict3)
