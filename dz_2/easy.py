import random

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
print('\nЗадача №1\n')
fruits = ["яблоко", "банан", "киви", "арбуз"]
for num, fruit in enumerate(fruits):
    print('{}.{:>10}'.format(num, fruit))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

# Создание двух списков длины 10 заполненынх случайными числами от 0 до 9
print('\nЗадача №2\n')
spisok1 = [random.randint(0, 9) for i in range(0, 10)]
spisok2 = [random.randint(0, 9) for i in range(0, 10)]

print('Список 1: ', spisok1)
print('Список 2: ', spisok2)
i = 0
while i < len(spisok1):
    if spisok1[i] in spisok2:
        del spisok1[i]
        # spisok1.remove(spisok1[i])
        i = 0
    else:
        i += 1
print('Итоговый список с удаленными элементами: ', spisok1)
# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

print('\nЗадача 3\n')

spisok = [random.randint(0, 9) for i in range(0, 10)]
print('Произвольный список: ', spisok)
spisok_new = []
for element in spisok:
    if element%2 == 0:
        spisok_new.append(element/4)
    else:
        spisok_new.append(element*2)

print('Новый список: ', spisok_new)
