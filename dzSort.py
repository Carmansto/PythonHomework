import  random

def myBubbleSort(myList):
        for i in range(len(myList)-1):
            for j in range(len(myList) - i - 1):
                if myList[j] > myList[j+1]:
                    temp = myList[j]
                    myList[j] = myList[j+1]
                    myList[j+1] = temp

def success(myList):
    while True:
        if len(myList)<10:
            break
        menu = input("Виведення оцінок - 1\nПерескладання іспиту - 2\nОтримання стипендії - 3\nВиведення відсортованого списку оцінок - 4\nДля виходу будь-яку іншу цифру\n")
        if menu == "1":
            for i,j in enumerate(myList):
                print(f"{i+1} - {j}")
        elif menu == "2":
            i = int(input("Введіть номер оцінки - "))
            j = input("Введіть нову оцінку - ")
            i -= 1
            myList[i] = j
            for i,j in enumerate(myList):
                print(f"{i+1} - {j}")
        elif menu == "3":
            if sum(myList) / len(myList) >= 10.7:
                print("Студент отримає стипендію")
            else:
                print("Студент не отримає стипендію")
        elif menu == "4":
            m = input("1 - за зростанням\n2 - за спаданняи\n")
            if m == "1":
                for i in range(len(myList) - 1):
                    for j in range(len(myList) - i - 1):
                        if myList[j] > myList[j + 1]:
                            temp = myList[j]
                            myList[j] = myList[j + 1]
                            myList[j + 1] = temp
            elif m == "2":
                for i in range(len(myList) - 1):
                    for j in range(len(myList) - i - 1):
                        if myList[j] < myList[j + 1]:
                            temp = myList[j]
                            myList[j] = myList[j + 1]
                            myList[j + 1] = temp
        for i, j in enumerate(myList):
            print(f"{i + 1} - {j}")

        else:
            break

def sortAdvanced(myList):
    for i in range(len(myList) - 1):
        swap = False
        print(f"{i+1}:")
        for j in range(len(myList) - i - 1):
            if myList[j] > myList[j + 1]:
                temp = myList[j]
                myList[j] = myList[j + 1]
                myList[j + 1] = temp
                swap = True
                print(f"Обмін {i} на {j+1}: {myList}")
        if not swap:
            print("Список відсортовано")
            break

print("\t\t\tЗавдання 1")

numbers = [random.randint(-50, 50) for i in range(11)]
d = len(numbers) // 3
leftNumbers = numbers[:d]
rightNumbers = numbers[d:]
d1 = len(rightNumbers) // 2
newNumbersTemp = rightNumbers[:d1]
newNumbersTemp1 = rightNumbers[d1:]
newNumbers = leftNumbers+newNumbersTemp
avrNumbers = sum(numbers) / len(numbers)
print(numbers)

if avrNumbers > 0:
    myBubbleSort(newNumbers)
    print(newNumbers+newNumbersTemp1[::-1])
else:
    myBubbleSort(leftNumbers)
    print(leftNumbers+rightNumbers[::-1])

print("\t\t\tЗавдання 2")
listGrades = []
for i in range(10):
    grade = int(input(f"Введіть {i+1} оцінку студена - "))
    if grade > 12 or grade < 1:
        print("Невірно введно оцінку")
        break
    else:
        listGrades.append(grade)

success(listGrades)

print("\t\t\tЗавдання 3")
list = [4,3,2,1,2,3,4,5,6,7,8,9,10]
sortAdvanced(list)
print(list)