#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

sum = int(0)
number = input("Enter real number: ")
for i in range(len(number)):
    if (number[i].isdigit()):
        sum += int(number[i])
print('The sum of the digits in a number =', sum)
print('\n')

#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

import math
number = int(input("Enter integer number: "))
setOfNumbers = [1]
for i in range(2,number+1):
    setOfNumbers.append(math.factorial(i))
print(setOfNumbers)
print('\n')

#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#Пример:
#- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

number = int(input("Enter integer number: "))
d = {a: a*3 + 1 for a in range(1,number+1)}
print(d)
print('\n')

#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#Реализуйте алгоритм перемешивания списка.

import random
number = int(input("Enter integer number: "))
setElements = []
for i in range(number):
    setElements.append(random.randint(-number,number))
print(setElements)
random.shuffle(setElements)
print(setElements)

