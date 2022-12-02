'''1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
стоящих на нечётной позиции.'''

x = [8, 11, 2, 1, 22, 5, 14]
summ = 0
for i in range(1, len(x), 2):
    if i % 2 == 1:
        summ += x[i]
print(f"{x} - сумма элементов на нечетных позициях: {summ}")

'''2.Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
второй и предпоследний и т.д.'''


def mult_lst(lists):
    lst = len(lists) // 2 + 1 if len(lists) % 2 != 0 else len(lists) // 2
    new_lst = [lists[i] * lists[len(lists) - i - 1] for i in range(lst)]
    print(new_lst)


lists = [2, 3, 4, 5, 6]
mult_lst(lists)

'''3.Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
и минимальным значением дробной части элементов.'''

lst = list(map(float, input("Введите числа через пробел:\n").split()))
news_list = [round(i % 1, 2) for i in lst if i % 1 != 0]
print(max(news_list) - min(news_list))

'''4.Напишите программу, которая будет преобразовывать десятичное число в двоичное. '''

binary = ""
decimal = int(input("Введите число: "))
while decimal != 0:
    binary = str(decimal % 2) + binary
    decimal //= 2
print(binary)

'''5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.'''

nums = int(input('Введите число: '))


def get_fibonacci(n):
    fibo_num = []
    a, b = 1, 1
    for i in range(n - 1):
        fibo_num.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range(n):
        fibo_num.insert(0, a)
        a, b = b, a - b
    return fibo_num


fibo_num = get_fibonacci(nums)
print(get_fibonacci(nums))
print(fibo_num.index(0))
