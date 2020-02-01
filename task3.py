# 3. реализовать разложение числа на степени простых множителей (ввод через input, выход по 0)

lst = []
while True:
    line = input('')
    lst.append(line)
    if line == '0':
        break
x = int(lst[0])


i = 2
cnt = 0
multipliers = []
while x > i:
    if x % i == 0:
        multipliers.append(i)
        x /= i
        cnt += 1
    else:
        print(i, '^', cnt, ' * ', sep='', end='') if cnt > 1 else None
        print(i, ' * ', sep='', end='') if cnt == 1 else None
        cnt = 0
        i += 1
print(i)
