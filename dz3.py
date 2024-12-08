#Завдання 1
n1 = int(input('Введіть перше число діапазону:'))
n2 = int(input('Введіть останнє число діапазону:'))

sum_p = 0
sum_n = 0
sum_k = 0
count_p = 0
count_n = 0
count_k = 0

for n in range(n1,n2+1):
    if n%2 == 0:
        sum_p += n
        count_p += 1
    else:
        sum_n += n
        count_n += 1
    if n%9 == 0:
        sum_k  += n
        count_k += 1

print(f"Сума парних чисел={sum_p}")
print(f"Сума непарних чисел={sum_n}")
print(f"Сума кратних 9-ти чисел={sum_k}")
avrg1 = sum_p/count_p if count_p > 0 else 0
avrg2 = sum_n/count_n if count_n > 0 else 0
avrg3 = sum_k/count_k if count_k > 0 else 0
print(f"Середньоарифметичне парних чисел = {avrg1}")
print(f"Середньоарифметичне непарних чисел = {avrg2}")
print(f"Середньоарифметичне кратних 9-ти чисел = {avrg3}")

#Завдання 2
d = int(input("Введіть довжину лінії:"))
s = input("Введыть символ, яким заповнити дыапазон:")

for c in range(d):
    print(s)

#Завдання 3

n = int(input("Введіть число:"))

while True:
    if n == 7:
        print("Goodbye")
        break
    elif n>0:
        print("Number is positive")
    elif n<0:
        print("Number is negative")
    else:
        print("Number is equal zero")
    n = int(input("Введіть число:"))

#Завдання 4
max_n = 0
min_n = 0
sum_n = 0
while True:
    num = int(input("Введіть число "))
    if num == 7:
        print("Good bye!")
        break
    sum_n+=num
    if max_n == 0 or num>max_n:
        max_n = num
    elif min_n == 0 or num<min_n:
        min_n = num
    else:
        continue

print(f"Сума чисел ={sum_n}")
print(f"Мінімальне значення ={min_n}")
print(f"Максимальне значення ={max_n}")




