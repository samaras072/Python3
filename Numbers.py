import os

def inst():
    print('Bir reqem fikirlewin(100-999999 kimi)')
    print()
    print('Fikirlewdiyiviz reqemde, reqemlerin yerini deyiwdirin')
    print()
    print('Mesel ucun 255 |Deyiwdirdikden sonram olur 525 yada 552|')
    print()
    print('Siz fikirlewdiyivznen yerini deyiwdirdiyiniz reqlemlerden')
    print()
    print('Cox olan reqemnen az olani cixin|Mesel ucun 525 - 255=270|')
    print()
    print('Ve alinan cavabdan bir reqem secin')
    print()
    print('Mesel ucun 270-den men sifiri secdim,qalan 27 oldu')
    print()
    print('Ve qalan reqemi awagi daxil edin')
    print()


a = input("Qalan reqemi daxil et:")
s = []

os.system('cls')

def append():
    while a.isalpha():
        print('Men sizi bawa duwe bilmirem')
        append()
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
        resume()
    elif b % 9 != 0:
        while b % 9 != 0:
            b+=1
            k+=1
        print('Siz secdiyiviz reqem %s' % (k))
        resume()
    os.system('pause')

def resume():
    ans = input('Tezeden bawlamag isteyirsiniz? |B/X|').lower()
    while ans != 'y' or ans!='yes' or ans!='да' or ans!='д' or ans!='n' or ans != 'no' or ans!='н' or ans!='нет' or ans!= 'b' or ans!='beli' or ans!='x' or ans!='xeyr':
        if ans == 'y' or ans ==  'yes' or ans=='да' or ans=='д' or ans=='b' or ans=='beli':
            append()
        elif ans=='n' or ans == 'no' or ans=='н' or ans=='нет' or ans=='x' or ans=='xeyr':
            print('Sagolun')
            os.system('pause')
            quit()
        else:
            print('Sizi bawa duwmurem')
            resume()

inst()
append()