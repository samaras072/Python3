a = []
b = int(input('Количество цифр в ответе:'))

def append():
    print('Например если ответ 421, то вводим цифры по одной 4 потом 2 потом 1')
    for i in range(b):
        a.append(int(input('Ваши цифры в ответе, запишите по одному:')))
    summary(a)

def summary(a):
    b = 0
    k = 0
    for z in a:
        b += z
    while b % 9 != 0:
        b+=1
        k+=1
    print(k)


append()