# 1. дан список [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]
#    1.1 найти максимум, минимум и их индексы в массиве
#    1.2 найти три самых часто встречаемых элемента массива
#    1.3 преобразовать в список где каждое значение будет встречаться только 1 раз
#       1.3.1 порядок не сохранялся
#       1.3.2 порядок сохранялся

a = [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]
i = max(a)
j = min(a)
print('Список:', a)
print('Максимум:', i, '\nМинимум:', j, '\nИндекс максимума:', a.index(i), '\nИндекс минимума:', a.index(j))
lst1 = list(a)
f = 1


def frequency(lst1):
    cnt_1 = 0
    c1 = 0
    x = 1
    for element in lst1:
        cnt = lst1.count(element)
        if cnt > cnt_1:
            cnt_1, c1 = cnt, element
            while x < cnt:
                lst1.remove(c1)
                cnt -= 1
    return c1, '   Количество: %s' % cnt_1


while f < 4:
    r = frequency(lst1)
    print('Частовстречаемый элемент №', f, ': ', r[0], r[1], sep='')
    f += 1
print('1.3.1 порядок не сохранялся:', lst1, '\n1.3.2 порядок сохранялся:', list(dict.fromkeys(a)))
