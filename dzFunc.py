from os import remove
from random import randint



def dobNumber(numbers):
    dob = 0
    for i in numbers:
        dob *= i
    return dob

def minNumber(numbers):
    minN = numbers[0]
    for i in numbers:
        if i < minN:
            minN = i
    return minN

def primeNumber(num):
    if num <= 1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def primeNumberCount(*numbers):
    primeCount = 0
    for i in numbers:
        if primeNumber(i):
            primeCount += 1
    return primeCount

def removeNumber(numbers):
    removeCount = 0
    a = int(input("Введіть число яке потрібно видалити - "))
    while a in numbers:
        numbers.remove(a)
        removeCount += 1

    return removeCount,a

def upList(list1,list2):
    list1.extend(list2)
    return list1

def stepList(list1,step):
    list2 = list(map(lambda x:x**step,list1))
    return list2
print("\t\t\tЗаданий список чисел")
numberList = [randint(-10,10) for i in range(10)]
print(numberList)
print("\t\t\tЗавдання 1")
print(f"Добуток чисел = {dobNumber(numberList)}")
print("\t\t\tЗавдання 2")
res = minNumber(numberList)
print(f"Мінімальне значення = {res}")
print("\t\t\tЗавдання 3")
res = primeNumberCount(1,2,3,4,5,6,7,8,9,10,11)
print(f"Кількість простих чисел = {res}")
print("\t\t\tЗавдання 4")
numberList1 = [1,2,3,1,2,3,1,2,3]
print(numberList1)
res,a= removeNumber(numberList1)
print(f"Число {a} видалено {res} рази")
print(numberList1)
print("\t\t\tЗавдання 5")
upList(numberList,numberList1)
print(numberList)
print("\t\t\tЗавдання 6")
print(numberList)
res = stepList(numberList,2)
print(res)