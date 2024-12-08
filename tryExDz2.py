
def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)

def factorial_upd(x):
    try:
        if x < 0:
            raise ValueError("Число має бути більше 0")
        else:
            if x == 0 or x == 1:
                return 1
            else:
                return x * factorial(x - 1)
    except Exception as e:
        return e

print("---Завдання 1, 2.1---")
try:
    x = int(input("Введіть число для пошуку факторілу: "))
    if x < 0:
        raise ValueError("Число має бути більше 0")
    else:
        print(factorial(x))
except Exception as e:
    print(e)

print("---Завдання 2.2---")
x = int(input("Введіть число для пошуку факторілу: "))
print(factorial_upd(x))


def show_list(num_list):
    print(num_list)
    print("Список по індексах:")
    for index, value in enumerate(num_list, start=0):
        print(f"Index: {index}, Value: {value}")

def max_num(num_list):
    max_n = num_list[0]
    for i in num_list:
        if i > max_n:
            max_n = i
    return max_n

def min_num(num_list):
    min_n = num_list[0]
    for i in num_list:
        if i < min_n:
            min_n = i
    return min_n

def show_index(num_list):
    index = int(input("Введіть індекс списку,для відображення, починаючи з 0: "))
    return num_list[index]

def remove_index(num_list):
    index = int(input("Введіть індекс списку,для видалення, починаючи з 0: "))
    del num_list[index]
    return num_list

def show_index_upd(num_list):
    index = int(input("Введіть індекс списку,для відображення, починаючи з 0: "))
    try:
        return num_list[index]
    except Exception as e:
        return e

def remove_index_upd(num_list):
    index = int(input("Введіть індекс списку,для видалення, починаючи з 0: "))
    try:
        del num_list[index]
        return num_list
    except Exception as e:
        return e

def main():
    num = input("Введіть числа через пробіл для списку: ")
    num_list = [float(x) for x in num.split()]
    while True:
        m = int(input(
            "Введіть число для дії:\nПоказати список - 1\nМаксимальне зачення - 2\nМінімальне значення - 3\nВивести число по індексу - 4\nВидалити чисо по індексу - 5\nВийти - 0\n"))
        if m == 1:
            show_list(num_list)
        if m == 2:
            print(max_num(num_list))
        if m == 3:
            print(min_num(num_list))
        if m == 4:
            try:
                print(show_index(num_list))
            except IndexError:
                print("Wrong index, out of range")
            except ValueError:
                print("Index can be only int")

        if m == 5:
            try:
                print(remove_index(num_list))
            except IndexError:
                print("Wrong index, out of range")
            except ValueError:
                print("Index can be only int")
        if m == 0:
            break

def main_new():
    num = input("Введіть числа через пробіл для списку: ")
    num_list = [float(x) for x in num.split()]
    while True:
        m = int(input(
            "Введіть число для дії:\nПоказати список - 1\nМаксимальне зачення - 2\nМінімальне значення - 3\nВивести число по індексу - 4\nВидалити чисо по індексу - 5\nВийти - 0\n"))
        if m == 1:
            show_list(num_list)
        if m == 2:
            print(max_num(num_list))
        if m == 3:
            print(min_num(num_list))
        if m == 4:
            print(show_index_upd(num_list))
        if m == 5:
            print(remove_index_upd(num_list))
        if m == 0:
            break

print("---Завдання 3,4.1---")
main()
print("---Завдання 4.2---")
main_new()