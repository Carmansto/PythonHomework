
tupleNum1 = {1,2,3,4,6}
tupleNum2 = {6,2,7,3,6}
tupleNum3 = {0,2,1,3,6}

for i in tupleNum1:
    if i in tupleNum1 and i in tupleNum2 and i in tupleNum3:
        print(f"Елемент {i} є в усіх кортежах")

uniqNum = []
for i in tupleNum1:
    if i in tupleNum1 and i not in tupleNum2 and i not in tupleNum3:
        uniqNum.append(i)
for i in tupleNum2:
    if i in tupleNum2 and i not in tupleNum1 and i not in tupleNum3:
        uniqNum.append(i)
for i in tupleNum3:
    if i in tupleNum3 and i not in tupleNum1 and i not in tupleNum2:
        uniqNum.append(i)

print(f"Унікальні елемнти: {uniqNum}")

def tupleNumI(tup1,tup2,tup3):
    set1 = set(tup1)
    set2 = set(tup2)
    set3 = set(tup3)

    tupNum = set1.intersection(set2,set3)

    return tupNum

print(f"Елементи, які є в кожному з кортежів і знаходяться в кожному з них на тій самій позиції:"
      f" {list(tupleNumI(tupleNum1,tupleNum2,tupleNum3))}")