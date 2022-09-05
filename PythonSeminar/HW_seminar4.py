import math
import random

#Вычислить число c заданной точностью d
#Пример:
#- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

def func1():
    d = float(input("Enter precision (0.1 - 0,0000000001): "))
    #state = "nice" if is_nice else "not nice"
    d = 0.1 if (d>0.1) else d
    d = 10**-10 if (d<10**-10) else d
    prec = len(str(d).split(".")[1])
    p = round(math.pi, prec)
    print(f'If precision = {d}, π = {p}\n')

#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def func2():
    n_num = int(input("Enter natural number: "))
    prime_factors = [1]
    for i in range(2,int(n_num+1/2)):
        if not n_num%i:
            prime_factors.append(i)
    print(f'For number = {n_num}, prime factors are: {prime_factors}\n')

#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def func3():
    list_3 = [4, 3, 3, 8, 7, 1, 5, 1, 8, 6, 9, 3, 7, 10, 6]
    print(f'For sequence {list_3}, sequence of unique values: {set(list_3)}\n')

#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл 
#многочлен степени k.
#Пример:
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

def func4():
    k = int(input("Enter natural power of a number: "))
    for i in range(k, -1, -1):
        coef = random.randint(0, 100)
        if coef:
            if i == k and i > 1:
                polynom = str(coef) + "*x^" + str(i)
            elif i == 1:
                polynom += " + " + str(coef) + "*x"
            elif i == 0:
                polynom += " + " + str(coef)
            else:
                polynom += " + " + str(coef) + "*x^"+str(i)
    polynom += " = 0"
    #print(polynom)
    with open('text.txt', 'w') as f:
        f.write(polynom)
    with open('text.txt', 'r') as f:
        print(f'Reading from file: {f.read()}\n')

#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def polinom_read_from_file(file_name):
    with open(file_name, 'r') as f:
        file_str = f.read()
    pol_list = file_str.split(" + ")
    pol_list.reverse()
    pol_list[0] = str(pol_list[0].split(" = ")[0])
    pol_dict = {}
    for i in range(len(pol_list)):
        if pol_list[i].find("^") != -1:
            pol_dict[int(pol_list[i].split("^")[1])] = int(pol_list[i].split("*")[0])
        elif pol_list[i].find("*") != -1:
            pol_dict[int(1)] = int(pol_list[i].split("*")[0])
        else:
            pol_dict[int(0)] = int(pol_list[i])
    return pol_dict

def func5():
    polynom_dict_1 = polinom_read_from_file("text.txt")
    polynom_dict_2 = polinom_read_from_file("text1.txt")
    max_power = max(polynom_dict_1) if max(polynom_dict_1) > max(polynom_dict_2) else max(polynom_dict_2)
    polynom_dict_sum = {}
    for i in range(max_power+1):
        polynom_dict_sum[i] = 0
        if i in polynom_dict_1:
            polynom_dict_sum[i] += polynom_dict_1[i]
        if i in polynom_dict_2:
            polynom_dict_sum[i] += polynom_dict_2[i]
    polinom_list = []
    for key in polynom_dict_sum:
        if key == 0:
            polinom_list.append(str(polynom_dict_sum[key]))
        elif key == 1:
            polinom_list.append(str(polynom_dict_sum[key])+"*x")
        else:
            polinom_list.append(str(polynom_dict_sum[key])+"*x^"+str(key))
    polinom_list.reverse()
    for i in range(len(polinom_list)):
        if i == 0:
            polynom_sum = polinom_list[i]
        else:
            polynom_sum += " + " + polinom_list[i]
    polynom_sum += " = 0"
    print(f'Sum of polynomials (read from file): {polynom_sum}\n')

#main
func1()
func2()
func3()
func4()
func5()