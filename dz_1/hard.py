# Создайте программу медицинская анкета, где вы запросите у пользователя такие данные, как имя, фамилию, возраст, и вес.
# И выведите результат согласно которому пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется начать вести правильный образ жизни, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии =)
# Формула не отражает реальной действительности и здесь используется только ради примера.

# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!

med_anketa = {}
med_anketa['name'] = input('Введите имя пациента: ')
med_anketa['age'] = int(input('Введите возраст: '))
med_anketa['weight'] = int(input('Введите вес: '))
# med_anketa = {'name':'Вася Пупкин', 'age':45, 'weight':140}


if med_anketa['age'] <= 30 and med_anketa['weight'] >= 50 and med_anketa['weight'] <= 120:
    print('Пациента в хорошем состоянии')
elif (med_anketa['age'] > 30 and med_anketa['age'] <= 40) and (med_anketa['weight'] < 50 or med_anketa['weight'] > 120):
    print('Пациенту нужно вести правильный образ жизни')
elif med_anketa['age'] > 40 and (med_anketa['weight'] < 50 or med_anketa['weight'] > 120):
    print('Пациенту требуется врачебный осмотр')
else:
    print('Неизвестный случай!!!')
