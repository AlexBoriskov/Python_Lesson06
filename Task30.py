# # Задача 30:  Заполните массив элементами арифметической прогрессии. 
# # Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# # Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# # Каждое число вводится с новой строки.

def tryType (num):
    while type(num) != int:
        try:
            num = int(num)
        except ValueError:
            print ("Ошибка")
            num = input ("Введите повторно число: ")
    return num

element01 = input ("Введипе I элемент: ")
element01 = tryType(element01)

diff = input ("Введите разность: ")
diff = tryType(diff)

size = input ("Количество элементов: ")
size = tryType(size)
while tryType(size)<0:
    print ("Число отрицательное. Ошибка!")
    size = input("Введите число: ")
    size = tryType(size)

ariflist = []

for i in range(size):
    c = element01 + i*diff
    ariflist.insert(i,c)

print (ariflist)

