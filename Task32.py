# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

def tryType (num):
    while type(num) != int:
        try:
            num = int(num)
        except ValueError:
            print ("Ошибка!")
            num = input ("Введите повторно: ")
    return num

def newArray (size, array):
    for i in range(size):
        array.append(randint(-100,100))
    return array


size = input ("Введите размер списка: ")
size = tryType(size)
while size < 0:
    print ("Размер не может быть меньше 0")
    size = input ("Введите размер массива: ")
    size = tryType(size)

spisok = []

spisok = newArray(size, spisok)
print (spisok)

minvalue = input ("Введите нижний порог: ")
minvalue = tryType(minvalue)

maxvalue = input("Введите верхний порог: ")
maxvalue = tryType(maxvalue)

if maxvalue<minvalue: minvalue, maxvalue = maxvalue, minvalue

result = []
for i in range(len(spisok)):
    if spisok[i]>minvalue and spisok[i]<maxvalue:
        result.append(i)

print (result)