# Задача: используя цикл запрашивайте у пользователя число пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степерь 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число не верное,
# и сообщаете об диапазоне допустимых. И просите ввести заного.
# Допустим пользователь ввел 2, оно подходит, возводим в степень 2, и выводим 4

# Задача-1

while True:
    n = int(input('Введите число: '))
    if (n >= 0 and n <= 10):
        print('Квадрат числа: ', n ** 2)
        break
    else:
        print('Число неверное. Введите число в диапазоне от 0 до 10')