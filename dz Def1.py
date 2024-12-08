
def vuvid():
    print("""““Don’t compare yourself with anyone in this world…
 if you do so, you are insulting yourself.”
Bill Gate""")

def par(a,b):
    number = []
    for i in range(a,b):
        if i%2 == 0:
            number.append(i)
    print(number)

def square(d,s,n):
    if n == True:
        for i in range(d):
                print(s*d)
    else:
        for i in range(d):
                if i == 0 or i == d - 1:
                    print(s*d)
                else:
                    d1=d-2
                    print(s+" "*d1+s)

def minN(a,b,c,d,e):
    if a<b<c<d<e:
        print(a)
    elif b<a<c<d<e:
        print(b)
    elif c<a<b<d<e:
        print(c)
    elif d<a<b<c<e:
        print(d)
    else:
        print(e)

def dobN(a,b):
    if b>a:
        dob = 0 + a
        for i in range(a,b+1):
            dob *= i
    else:
        c = a
        a = b
        b = c
        dob = 0 + a
        for i in range(a, b + 1):
            dob *= i
    print(dob)

def sumN(a):
    sumNum = 0
    for i in range(len(str(a))):
        sumNum += 1

    print(f"Кільість цифер у числі {a} = {sumNum}")

def polindrom(a):
    strA = str(a)
    if strA == strA[::-1]:
        print(f"Число {a} є поліндромом")
        return True
    else:
        print(f"Число {a} не поліндром")
        return False

print("----------task1----------")
vuvid()
print("----------task2----------")
par(0,15)
print("----------task3----------")
square(7,"*",False)
print("\n----------task4----------")
minN(4,5,-4,21,-53)
print("----------task5----------")
dobN(5,1)
print("----------task6----------")
sumN(123123)
print("----------task7----------")
polindrom(123321)