#Завдання 1
str1 = input("Введіть рядок для перевірки:")
if str1 == str1[::-1]:
    print(f"Рядок \"{str1}\" є паліндромом.")
else:
    print(f"Рядок \"{str1}\" не паліндром")

#Завдання 2
str1 = input("Введіть текст :")
res_words = input("Введіть список слів через кому(приклад: небо,сонце,місяць):")
for word in str1.split():
    if word.lower() in res_words:
        str1 = str1.replace(word, word.upper())

print(str1)

#Завдання 3
text = input("Введіть текст:")
answ = text.count(".")+text.count("!")+text.count("?")
print(f"Кількість пропозицій в тексті = {answ}")
