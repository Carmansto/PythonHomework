def greeting(name, age):
    return f"Привіт, {name}! Твій вік - {age}"

def greeting_upd(name, age):
    try:
        if (age < 0) or (age > 130):
            raise ValueError("Вік повинен бути > 0 та < 130")
        else:
            return f"Привіт, {name}! Твій вік - {age}"
    except Exception as e:
        print(e)

print("---Завдання 1,2.1")
try:
    name = input("Введіть ім'я: ")
    age = int(input("Введіть вік: "))
    if (age < 0) or (age > 130):
        raise ValueError("Вік повинен бути > 0 та < 130")
    else:
        print(greeting(name, age))
except Exception as e:
    print(e)

print("---Завдання 2.2")
name = input("Введіть ім'я: ")
age = int(input("Введіть вік: "))
print(greeting_upd(name, age))

print("---Завдання 3, 4.1")
def check_numbers(num_list):
    return sum(num_list)

num = input("Введіть числа для списку через пробіл: ")
number_list = [float(i) for i in num.split()]
print("Заданий список:")
print(number_list)
try:
    if any(i < 0 for i in number_list):
        raise ValueError("В списку є від'ємні числа")
    else:
        print(check_numbers(number_list))
except Exception as e:
    print(e)



def check_numbers_upd(num_list):
    try:
        if any(i < 0 for i in num_list):
            raise ValueError("В списку є від'ємні числа")
        else:
            return sum(num_list)
    except Exception as e:
        return e

print("---Завдання 4.2")
num = input("Введіть числа для списку через пробіл: ")
number_list = [float(i) for i in num.split()]
print("Заданий список:")
print(number_list)
print(check_numbers_upd(number_list))