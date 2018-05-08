# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.
def salary_write(dict_salary, file_name='salary.txt'):
    with open(file_name, 'w', encoding='UTF-8') as file_salary:
        for key, value in dict_salary.items():
            file_salary.write(key + ' - ' + str(value) + '\n')


def salary_read(file_name='salary.txt'):
    dict_salary = {}
    with open(file_name, encoding='UTF-8') as file_salary:
        for line in file_salary:
            line = line.strip()
            line = line.split(' - ')
            dict_salary[line[0]] = int(line[1])
    return dict_salary


names = ['Иван', 'Виктор', 'Анна', 'Леонид', 'Александр']
salary = [130000, 170000, 46000, 750000, 632000]

print('Имена: ', names)
print('Зарплаты: ', salary)

dict_salary = dict(zip(names, salary))

salary_write(dict_salary)
print('\nФайл записан\n')

dict_salary = salary_read()
print('Файл прочитан\n')
for key, value in dict_salary.items():
    if value < 500000:
        print('ЗП сотрудника: ', key.upper(), value * 0.87)
