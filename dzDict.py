print("\t\t\tЗавдання 1")

basketballDict = {"M.J":1.98,"L.J":2.06,"W.C":2.16,"O.R":1.96}
print(f"Початковий список {basketballDict}")
while True:
    m = input("Виберіть дію:\nДодати - 1\nВидалити - 2\nПошук - 3\nЗаміна - 4\nДля переходу до наступного завдання - 0\n")
    if m == "1":
        a = input("Введіть ініціали баскетболіста: ")
        b = input("Введіть зріст: ")
        basketballDict[a] = b
        print(basketballDict)
    elif m == "2":
        a = input("Введіть ініціали для видалення: ")
        if a in basketballDict:
            del basketballDict[a]
        else:
            print("Ініціалів не знайдено")
        print(basketballDict)
    elif m == "3":
        a = input("Введіть ініціали для пошку: ")
        print(basketballDict.get(a))
    elif m == "4":
        a = input("Ведіть ініціали для заміни: ")
        b = input("Ведіть зріст для заміни: ")
        basketballDict[a] = b
        print(basketballDict)
    else:
        break

print("\t\t\tЗавдання 2")

translateDict = {"word":"mot","number":"nombre","programming":"programmation","school":"ecole"}
print(f"Початковий список {translateDict}")
while True:
    m = input("Виберіть дію:\nДодати - 1\nВидалити - 2\nПошук - 3\nЗаміна - 4\nДля переходу до наступного завдання - 0\n")
    if m == "1":
        a = input("Введіть слово англійською: ").lower()
        b = input("Переклад французбкою: ").lower()
        translateDict[a] = b
        print(translateDict)
    elif m == "2":
        a = input("Введіть слово для видалення(англ): ").lower()
        if a in translateDict:
            del translateDict[a]
        else:
            print("Слово не знайдено")
        print(translateDict)
    elif m == "3":
        a = input("Введіть слово для пошку: ").lower()
        print(translateDict.get(a))
    elif m == "4":
        a = input("Ведіть слово(англ) для заміни: ").lower()
        b = input("Ведіть слово(франц) для заміни: ").lower()
        translateDict[a] = b
        print(translateDict)
    else:
        break

print("\t\t\tЗавдання 3")

companyDict = {"Х.А.В":{"Телефон":"0689545922","email":"khomiakav@gmail.com","Посада":"Су-шеф","Номер офісу":"777","skype":"none"}}
print(companyDict)
while True:
    m = input("Виберіть дію:\nДодати - 1\nВидалити - 2\nПошук - 3\nЗаміна - 4\nДля переходу до наступного завдання - 0\n")
    if m == "1":
        name = input("Введіть ПІБ: ")
        phone = input("Введіть телефон: ")
        email = input("Введіть корпоративний email: ")
        position = input("Введіть назву посади: ")
        officeNum = input("Введіть номер кабінету: ")
        skype = input("Введіть Skype: ")
        companyDict[name] = {
            "Телефон": phone,
            "email": email,
            "Посада": position,
            "Номер офісу": officeNum,
            "skype": skype
        }
        print(companyDict)
    elif m == "2":
        name = input("Введіть ім'я для видалення")
        if name in companyDict:
            del companyDict[name]
            print("Працівника видалено")
        else:
            print("Працівника не знайдено")
        print(companyDict)
    elif m == "3":
        name = input("Введіть ім'я для пошуку")
        if name in companyDict:
            print("Інформація про працівника:")
            for i,j in companyDict[name].items():
                print(f"{i}:{j}")
    elif m == "4":
        name = input("Введіть ПІБ працівника для оновлення інформації: ")
        if name in companyDict:
            print("Що ви хочете оновити?")
            print("Телефон - 1")
            print("Email - 2")
            print("Назву посади - 3")
            print("Номер кабінету - 4")
            print("Skype - 5")
            m = input("Введіть номер опції: ")

            if m == "1":
                companyDict[name]["Телефон"] = input("Введіть новий телефон: ")
            elif m == "2":
                companyDict[name]["email"] = input("Введіть новий email: ")
            elif m == "3":
                companyDict[name]["Посада"] = input("Введіть нову назву посади: ")
            elif m == "4":
                companyDict[name]["Номер офісу"] = input("Введіть новий номер кабінету: ")
            elif m == "5":
                companyDict[name]["skype"] = input("Введіть новий Skype: ")
            else:
                print("Невірний вибір.")
            print("Інформацію оновлено")
            for i,j in companyDict[name].items():
                print(f"{i}:{j}")
        else:
            print("Працівника з таким ПІБ не знайдено.")
        print(companyDict)
    else:
        break

print("\t\t\tЗавдання 4")

libraryDict = {"J.K. Rowling":{"Назва книги":"Harry Potter","Жанр":"Fantasy","Рік випуску":"1997","Кількість сторінок":"223","Видавництво":"Bloomsbury"}}
print(libraryDict)
while True:
    m = input("Виберіть дію:\nДодати - 1\nВидалити - 2\nПошук - 3\nЗаміна - 4\nДля виходу - 0\n")
    if m == "1":
        name = input("Введіть автора: ")
        nameBook = input("Введіть назву книги: ")
        typeBook = input("Введіть жанр: ")
        year = input("Введіть рік випуску: ")
        countBook = input("Введіть кількість сторінок: ")
        pub = input("Введіть видавництво: ")
        libraryDict[name] = {
            "Назва книги": nameBook,
            "Жанр": typeBook,
            "Рік випуску": year,
            "Кількість сторінок": countBook,
            "Видавництво": pub
        }
        print(libraryDict)
    elif m == "2":
        name = input("Введіть ім'я для видалення")
        if name in libraryDict:
            del libraryDict[name]
            print("Книгу видалено")
        else:
            print("Книгу не знайдено")
        print(libraryDict)
    elif m == "3":
        name = input("Введіть ім'я для пошуку")
        if name in libraryDict:
            print("Інформація про книгу:")
            for i,j in libraryDict[name].items():
                print(f"{i}:{j}")
    elif m == "4":
        name = input("Введіть ім'я автора для оновлення інформації: ")
        if name in libraryDict:
            print("Що ви хочете оновити?")
            print("Назву книги - 1")
            print("Жанр - 2")
            print("Рік випуску - 3")
            print("Кількість сторінок - 4")
            print("Видавництво - 5")
            m = input("Введіть номер опції: ")

            if m == "1":
                libraryDict[name]["Назва книги"] = input("Введіть нову назву: ")
            elif m == "2":
                libraryDict[name]["Жанр"] = input("Введіть новий жанр: ")
            elif m == "3":
                libraryDict[name]["Рік випуску"] = input("Введіть новий рік випуску: ")
            elif m == "4":
                libraryDict[name]["Кількість сторіеок"] = input("Введіть нову кількість сторінок: ")
            elif m == "5":
                libraryDict[name]["Видавництво"] = input("Введіть нове видавництво: ")
            else:
                print("Невірний вибір.")
            print("Інформацію оновлено")
            for i,j in libraryDict[name].items():
                print(f"{i}:{j}")
        else:
            print("Автора не знайдено")
        print(libraryDict)
    else:
        break