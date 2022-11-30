import random
from random import randint

''' 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.'''

sum = 0
num = input('Введите число: ')

for i in num:
    if i.isdigit():
        sum += int(i)

print(sum)

'''2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N'''

input_num = int(input('Введите число: '))
temp_num = 1

for i in range(input_num):
    temp_num *= i + 1
    print(temp_num, end=' ')

'''3.Задайте список из n чисел последовательности (1 + 1 / n)**n и выведите на экран их сумму.'''

n = int(input('Введите количество чисел: '))


def number(n):
    summ = 0
    for i in range(n):
        a = int(input(f'Введи число {i + 1} '))
        a = (1 + 1 / a) ** a
        summ = a + summ
        i += 1
    return summ


print('Сумма чисел равна', round((number(n)), 2))

'''4.Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.'''

numbers = []
for i in range(10):
    numbers.append(randint(-10, 10))
print(numbers)


def get_numbers(numbers):
    count = 0
    for element in numbers:
        count += 1
    return count


print('Всего элементов: ', get_numbers(numbers))

x = int(input('Введите номер первого элемента: '))
y = int(input('Введите номер второго: '))

for i in range(len(numbers)):
    mult = numbers[x - 1] * numbers[y - 1]
print(f'Произведение этих элементов: {numbers[x - 1]} * {numbers[y - 1]} =', mult)

'''5. Реализуйте алгоритм перемешивания списка.
Из библиотеки random использовать можно только randint'''

length = 15
list = [i for i in range(length)]

print(list)

for i in range(len(list)):
    r = random.randint(i, length - 1)
    m = list[i]
    list[i] = list[r]
    list[r] = m

print(list)
