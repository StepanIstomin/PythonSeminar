#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

set_1 = [1,2,3,4,5,6,7,8,9]
odd_sum = int(0)
for i in range(1,len(set_1),2):
    odd_sum += set_1[i]
print(f'{set_1} Sum of odd numbers = {odd_sum}\n')

#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
set_2=[]
for i in range(int(len(set_1)/2)+int(len(set_1)%2)):
    set_2.append(set_1[i]*set_1[-1-i])
print(f'{set_1} => {set_2}\n')

#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
set_3=[1.1, -1.2, 3.1, -5, 10.01, -0.17]
set_3_frac = []
for i in range(len(set_3)):
    #print(set_3[i] - int(set_3[i]))
    #print(str(set_3[i]).find("."))
    if (str(set_3[i]).find(".") != -1):
        set_3_frac.append(float("0." + str(set_3[i]).split('.')[1]))
print(f'{set_3} MAX/MIN Fraction difference = {max(set_3_frac)-min(set_3_frac)}\n')

#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#предполагаю что использование bin() слишком банально?
dec_num = int(input("Enter integer decimal number: "))
bin_num = str()
while True:
    digit = int(dec_num%2)
    bin_num = str(digit) + bin_num
    dec_num =  int(dec_num/2)
    if (dec_num < 2):
        bin_num = str(dec_num)+ bin_num
        break
print(f'Binary number => {bin_num}\n')    

#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
n = int(input("Enter integer number(>0): "))
fib_pos = [0,1]
fib_neg = [1]
n_prev = int(0)
n_cur = int(1)
for i in range(2,n+1):
    fib_pos.append(n_prev+n_cur)
    n_prev = n_cur
    n_cur = fib_pos[i]
    fib_neg.append(-n_cur)
fib_neg.reverse();
negfib_seq = fib_neg + fib_pos
print(f'Negafibonacci sequence => {negfib_seq}\n')