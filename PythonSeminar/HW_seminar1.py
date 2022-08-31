
#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

day = int(input('Enter day of week (1-7): '))
if (day == 6 or day == 7):
	print('This is weekend day')
else:
	print('This is not weekend day')
print('\n')

#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = input('X: ')
y = input('Y: ')
z = input('Z: ')
print('¬(X V Y V Z) = ¬X ⋀ ¬Y ⋀ ¬Z', end="")
if (not(x or y or z) == (not x and not y and not z)):
	print(' - TRUE')
else:
	print(' - FALSE')
print('\n')

#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
#в которой находится эта точка (или на какой оси она находится).

x = int(input('X: '))
y = int(input('Y: '))

if (x > 0 and y > 0):
	print ('-> 1')
elif (x < 0 and y > 0):
	print ('-> 2')
elif (x < 0 and y < 0):
	print ('-> 3')
elif (x > 0 and y < 0):
	print ('-> 4')
else:
	print('Point is on axis')
print('\n')

#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Enter quarter number(1-4): '))
if (quarter == 1):
	print ('1-st quarter - x > 0 , y > 0')
elif (quarter == 2):
	print ('2-nd quarter - x < 0 , y > 0')
elif (quarter == 3):
	print ('3-rd quarter - x < 0 , y < 0')
elif (quarter == 4):
	print ('4-rd quarter - x > 0 , y < 0')
else:
	print('Wrong number!')
print('\n')

#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

ax = float(input('Enter x of point A: '))
ay = float(input('Enter y of point A: '))
bx = float(input('Enter x of point B: '))
by = float(input('Enter y of point B: '))
dist = ((bx-ax)**2+(by-ay)**2) ** 0.5
print('Distance between A and B is',dist)