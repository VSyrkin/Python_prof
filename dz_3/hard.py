# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, persoтn2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.
print('Задача №1\n')


def attack(person1, person2):
    person2['health'] = person2['health'] - person1['damage']
    return person1, person2


player = {'name': 'Игрок', 'health': 100, 'damage': 50}
# player['name'] = input('Введите имя игрока:')

enemy = {'name': 'Противник', 'health': 100, 'damage': 50}
# enemy['name'] = input('Введите имя противника:')
print('Исходное положение:')
print(player)
print(enemy)

player, enemy = attack(player, enemy)
print('\nПосле атаки {} на {}:'.format(player['name'], enemy['name']))
print(player)
print(enemy)

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.
print('\nЗадача №2\n')


def damage_with_armor(damage, armor):
    return round(damage / armor, 2)


def attack_with_armor(person1, person2):
    person2['health'] = round(person2['health'] - damage_with_armor(person1['damage'], person2['armor']), 2)
    return person1, person2


def write_person(person):
    with open(person['name'] + '.txt', 'w', encoding='UTF-8') as file_person:
        for key, value in person.items():
            file_person.write(key + ':' + str(value) + '\n')


def read_players(player_name, enemy_name):
    dict_player = {}
    with open(player_name + '.txt', encoding='UTF-8') as file_player:
        for line in file_player:
            line = line.strip()
            line = line.split(':')
            if line[0] == 'name':
                dict_player[line[0]] = line[1]
            else:
                dict_player[line[0]] = float(line[1])
    dict_enemy = {}
    with open(enemy_name + '.txt', encoding='UTF-8') as file_enemy:
        for line in file_enemy:
            line = line.strip()
            line = line.split(':')
            if line[0] == 'name':
                dict_enemy[line[0]] = line[1]
            else:
                dict_enemy[line[0]] = float(line[1])

    return dict_player, dict_enemy


player = {'name': 'Игрок', 'health': 100, 'damage': 50, 'armor': 1.2}
# player['name'] = input('Введите имя игрока:')
enemy = {'name': 'Противник', 'health': 100, 'damage': 50, 'armor': 1.2}
# enemy['name'] = input('Введите имя противника:')

# Запись сущностй в файл
write_person(player)
write_person(enemy)

# Чтение из файла
player, enemy = read_players(player['name'], enemy['name'])

print('Данные загружены\nИгра начилась!\n')
# Игра
while player['health'] > 0 and enemy['health'] > 0:
    attack_with_armor(player, enemy)
    player, enemy = enemy, player

if player['health'] > 0:
    won = player
else:
    won = enemy

print('Победитель: ', won['name'], '\nосталось жизней: ', won['health'])
