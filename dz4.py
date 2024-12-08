# Завдання 1
n1 = int(input("Введіть число - "))
n2 = int(input("Введіть степінь - "))
s = n1 ** n2
print(f"Степінь числа {n1} = {s}")

# Завдання 2,3
lane = range(100,1000)
k1 = 0
k2 = 0
for c in lane:
    num = str(c)
    if num[0] == num[1] or num[1] == num[2] or num[0] == num[2]:
        k1+=1
    if num[0] != num[1] and num[1] != num[2] and num[0] != num[2]:
        k2+=1
print(f"Кількість чисел з двома одинаковими цифрами = {k1}")
print(f"Кількість чисел з різними цифрами = {k2}")


#Завдання 4
from idlelib.replace import replace
num = str(input("Введіть ціле число "))
num = num.replace("3", "")
num = num.replace("6", "")
print(num)