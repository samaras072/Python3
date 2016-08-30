import os

a = input("Qalan reqemi daxil et:")
s = []

os.system('cls')

def append():
    for i in range(len(a)):
        a.split()
        s.append(int(a[i]))
    summary(s)

def summary(s):
    b = 0
    k = 0
    for z in range(len(s)):
        b += s[z]
    if b % 9 == 0:
        print('Siz secdiyiviz reqem ya 0-di yadaki 9-dur')
    elif b % 9 != 0:
        while b % 9 != 0:
            b+=1
            k+=1
        print(k)

    os.system('pause')

append()
