# result = 0
# count = 0
# while True:
#     number = int(input('Введите число\n'))
#     if number >= 0:
#         result += number
#         count += 1
#     if number < 0:
#         break
#     print('Сумма чисел = ', result)
# print('Результат =', result / count)
import random

# result = 0
# while True:
#     number = int(input('Введите число\n'))
#     if number == 0:                      #and number % 2 == 1 or number < 0 and number % 2 == 1: 0 четный
#         break
#     if number % 2 == 0:
#         continue
#     result += number
# print('Сумма нечетных чисел = ', result)

# 6.4 операторы использовать
# 6.6 б + разность между ними
# 6.42 а

# 6.4
# result = 0
# while True:
#     number = int(input('Введите число\n'))
#     if number > 0:
#         break
#     result += 1
# print('Количество введенных отрицательных чисел =',result)

# 6.6 б
# while True:


# # 6.42 а
# number = int(input('Введите число\n'))
# maxNumber1 = 0
# maxNumber2 = 0
# index = 0
#
# indexMaxNumber1 = 0
# indexMaxNumber2 = 0
# number1 = number
# while number1 > 0:
#     x = number1 % 10 # переход в конец введенного числа
#     if x > maxNumber1:
#         maxNumber1 = x
#         indexMaxNumber1 = index
#     index += 1
#     number1 //= 10
# print(maxNumber1)
# print(indexMaxNumber1)
#
# number1 = number
# index = 0
# while number1 > 0:
#     x = number1 % 10
#     if x > maxNumber2 and x != maxNumber1:
#         maxNumber2 = x
#         indexMaxNumber2 = index
#     if x > maxNumber2:
#         maxNumber2 = x
#         indexMaxNumber2 = index
#     index +=1
#     number1 //= 10
# print(maxNumber2)
# print(indexMaxNumber2)

# number1 = 5
# number2 = 10
# summa = number1 + number2
# print(number1, '+', number2, '=', number1+number2)
# print(f'{number1} + {number2} = {summa}')

# Гоша Дударь itproger.com ютуб

# 9.14 9.15 9.16 9.24 9.38а 9.41 9,59 9,76 б
# дана строка вывести ее наоборот

# 9.14
# text = input('Введите слово\n')
# print(text[-1])

# 9.15
# text = input('Введите слово\n')
# number = int(input('Введите номер символа который нужно вывести\n'))
# print(text[number])

# 9.16
# text = input('Введите слово\n')
# if text[2] == text[4]:
#     print('Символы одинаковы')
# else:
#     print('Символы разные')

# 9.24
# text = 'Яблоко'
# print(text[1:5])
# print(text[3:6])

# 9.38а
# text = input('Введите слово из 12 букв\n')
# if len(text) <= 12:
#     print(text[8:12], text[4:8], text[0:4])
#     print(f'{text[8:12]}{text[4:8]}{text[0:4]}')
# else:
#     print('Ошибка ввели > 12 символов')

# 9.41
# print('Л\nо\nк\nо\nм\nо\nт\nи\nв')
# text = input('Введите текст \n')
# text1 = len(text)
# while text1 < 10:
#     if text1 > 1:
#         print(text[0],'\n',text[1],'\n',text[2],'\n')


# text = input('Введите текст \n')
# text1 = len(text)
# count = 0
# summ = 0
# while count < text1:
#     if text[count] == 'и':
#         summ +=1
#     count +=1
# print(f'Количество и в строке {summ}')


# 9.59
# text = input('Введите текст \n')
# text1 = len(text)
# print(list(text))
# print(text[::-1])

# 9.76б
# someString = input('Введите текст \n')
# index = 0
# indexSymbol = 0
# lenString = len(someString)
# while index < lenString:
#     if someString[index] == 'j'
#         indexSymbol = index кол-во слов
#     index +=1
# print(indexSymbol + 1)

# text = input('Введите предложение \n')
# index = 0
# count = 1
# text1 = len(text)
# while index < text1:
#     if text[index] == ' ':
#         count += 1
#     index += 1
# print(f'Количество слов в предложении = {count}')

# text = input('Введите текст_ \n')
# text1 = input('Введите символ \n')
# print(text[:-1] + text1)

# 9.105 9.90 9.92 9.153-символ вводится с клавы и текст с клавы и сравнивается

#9.90
# text = input('Введите текст \n')
# i = 0
# newText = ''
# text2 = len(text)
# while i < text2:
#     if text[i] == 'е':
#         newText += 'и'
#     else:
#         newText += text[i]
#     i += 1
# print(newText)

#9.92
# text = input('Введите текст \n')
# i = 0
# newText = ''
# text2 = len(text)
# while i < text2:
#     if (i+1) % 2 == 0:
#         newText += 'ы'
#     else:
#         newText += text[i]
#     i += 1
# print(newText)

# 9.105
# text = input('Введите слово из 12 букв\n')
# if len(text) <= 12:
#     print(f'{text[3:10]}')
# else:
#     print('Ошибка ввели > 12 символов')

# 9.153
# text = input('Введите текст \n')
# text1 = input('Введите искомый символ \n')
# i = 0
# a = 0
# b = 0
# text2 = len(text)
# while i < text2:
#     if text[i] == text1:
#         a += 1
#         b = a
#     i += 1
# print(a) #две пременные а потом 0 есле не та

#9.83
# someString = input('Введите текст \n')
# if ',' in someString:
#     indexFirst = someString.index(',')
#     str1 = someString[:indexFirst]
#     result = str1.count('n')
#     print(result)
# else:
#     print('ERROR')

# 9.82
# text = input('Введите текст \n')
# text3 = text.lstrip()
# i = 0
# newText = ''
# text2 = len(text3)
# while i < text2:
#     if text3[i] != ' ':
#         newText += text3[i]
#         # newText.count('o')
#         i += 1
#     else:
#         break
# print('Количество букв о в 1 слове = ' ,newText.count('o'))

# 9.141
# text = input('Введите текст \n')
# text2 = len(text)
# i = 0
# digit = 0
# maks = 0
# while i < text2:
#     if text[i].isdigit():
#         digit += int(text[i])
#         num = int(text[i])
#         if num > maks:
#             maks = num
#     i += 1
# print(digit)
# print(maks)

# 9.161
# text = input('Введите текст \n')
# result = len(set(text))
# print(result)


# 9.166
# text = input('Введите текст \n')
# rf = text.rfind(' ') # правый пробел (последний)
# lf = text.find(' ') # первый пробел
# print(text[rf:], text[lf:rf], text[:lf])

# text = input('Введите текст \n')
# text1 = text.replace('с', '')
# print(text1)
# print(input('Введите текст \n').replace('c',''))

# text = input('Введите текст \n')
# result = text[: text.index(' ')].count('о')
# print(result)

# text = input('Введите текст \n')
# print((text.count('а')/len(text.replace(' ','')))*100)


# 2 строки 1 анаграмма другой

# text = input('Введите текст \n')
# result = text.count(' ') + 1 > 3
# print(result)

# text = input('Введите текст \n')
# result = text[: text.index(',')]  # с начала строки до ,
# print(result)

# text = input('Введите текст \n') # привет
# textDl = len(text)
# text1 = input('Введите текст \n')
# textDl1 = len(text1)
# if textDl == textDl1:
#     index = 0
#     letter = text[index]
#     while index < textDl:
#         if text.count(letter) != text1.count(letter):
#             print(False)
#             break
#         index += 1
#     print(True)
# else:
#     print(False)

# someList = [37, 0, 5]
# index = int(input('Введите индекс'))
# if index > len(someList):
#     print('Индекс за пределами списка')
# else:
#     print(someList[index])

# someList = [37, 0, 5]
# index = 0
# while index < len(someList):
#     someList[index] *= 2
#     index += 1
# print(someList)

# someList = [37, 0, 5]
# index = 0
# firstNumber = someList[0]  # для списка обязательно
# while index < len(someList):
#     someList[index] /= firstNumber
#     index += 1
# print(someList)

# someList = [37, 0, 5]
# sumNumber = sum(someList) # сумма списка
# print(sumNumber)

# someList = [37, 0, 5]
# sumNumber = sum(someList) / len(someList) # среднее арифм
# print(sumNumber)

# somList = ['Hello, World']
# print(somList[0][1]) # выведет 1 символ в первом слове

# max и min

# def countSumNumbers(number1, number2):
#     return number1 + number2
# result = countSumNumbers(1,2) # параметры number1, number2 цифры 1 , 2
# print(result)

# def countSqare(a, b):
#     return a * b
# width = 10
# hight = 20
# result = countSqare(width, hight)
# print(result)

# def countP(side1, side2, side3):
#     return side1 + side2 + side3
# number1 = 10
# number2 = 20
# number3 = 30
# result = countP(number1, number2, number3)
# print(result)

# def isPalindrome(number1, number2):
#     str1 = str(number1)
#     if str1 == str1[::-1]:
#         return  True
#     str2 = str(number2)
#     if str2 == str2[::-1]:
#         return True
#     return False
# num1 = int(input('Введите число\n'))
# num2 = int(input('Введите число\n')) разница макс и мин
# result = isPalindrome(num1, num2)
# print(result)

# def minNumber(Somlist):
#     minNumber = Somlist[0]
#     for item in Somlist:
#         if item < minNumber:
#             minNumber += 1
#     return minNumber
# def maxNumber(Somlist):
#     maxNumber = Somlist[0]
#     for item in Somlist:
#         if maxNumber < item:
#             maxNumber = item
#     return maxNumber
#
#
# list = [1, 2, 3, 4, 55]
# result = maxNumber(list) - minNumber(list)
# print(result)

# text = (1, 2, 3, 4) # кортеж
# result = tuple(Somstring) # превратить в кортеж
# result = list(Somstring) # превратить в список

# import random
# lenList = int(input())
# lenList = 5
#
# someList = []
# for i in range(lenList):
#     someList.append(random.randint(1, 100))
#
# print(someList)

# number = random.randint(1, 100)
# print(number)

# import random
# number = random.randint(1, 14)
# number2 = random.randint(1, 200)
# print(f'Домашнее задание: {number}.{number2}')

# import random
# lenList = 8
#
# someList = []
# for i in range(lenList):
#     someList.append(random.randint(1, 100))
#
# print(someList)
#
# def get_answer(arr):
#     list1 = []
#     for i in arr:
#         list1.append(i ** 2)
#         sum_arr = sum(list1)
#         if sum_arr // 100000 > 0:
#             return True
#         else:
#             return False
#
#
# import random
# lenList = 8
#
# someList = []
# for i in range(lenList):
#     someList.append(random.randint(1, 100))
# result = get_answer(someList)
#
# print(result)
# k = 15
# number = 1011121314151617181920212223242526272829303132333435363738394041424344454647484950
# def summa(number):
#     str1 = str(number)
#
#     return str1
#
# str1 = summa(number)
# print(str1[16])

#
# def delitel(num1):
#     someList = []
#     for i in range(num1):
#         if num1 % 2 == 0:
#             someList.append(num1)
#     someList.append(num1)
#     return someList
#
#
# import random
# num = random.randint(1, 100)
# result = delitel(num)
# print(result)

# lenList = 5
# someList = [''] * lenList
# print(someList)
#
# for index in range(lenList):
#     someList[index] = input()
# print(someList)

# import random
# lenX = 2
# lenY = 3
# matrix = [[]] * lenX
# for i in range(lenX):
#     matrix[i] = [0] * lenY
#     for j in range(lenY):
#         matrix[i][j] = random.randint(1, 9)
# for i in range(lenX):
#     print(matrix[i])

# сначала строка потом столбец

# import random
# lenX = int(input('Введите размер '))
# lenY = int(input('Введите размер '))
# matrix = [[]] * lenX
# for i in range(lenX):
#     matrix[i] = [0] * lenY
#     # print(matrix[i])
# for i in range(lenX):
#     for j in range(lenY):
#         matrix[i][j] = random.randint(10, 99)
# for i in range(lenX):
#     print(matrix[i])
#
# columNumber = int(input('Введите столбец'))
# if columNumber > lenY:
#     print('ok')
# else:
#     for i in range(lenX):
#         print(matrix[i][columNumber - 1], end=' ')

# import random
# lenX = int(input('Введите размер матрицы '))
# lenY = int(input('Введите размер матрицы '))
# matrix = [[]] * lenX
# for i in range(lenX):
#     matrix[i] = [0] * lenY
#     # print(matrix[i])
# for i in range(lenX):
#     for j in range(lenY):
#         matrix[i][j] = random.randint(10, 99)
# for i in range(lenX):
#     print(matrix[i])
# result = matrix[0][0] + matrix[0][2]
# print(result)

# import random
# lenX = int(input('Введите размер матрицы '))
# lenY = int(input('Введите размер матрицы '))
# matrix = [[]] * lenX
# for i in range(lenX):
#     matrix[i] = [0] * lenY
#     # print(matrix[i])
# for i in range(lenX):
#     for j in range(lenY):
#         matrix[i][j] = random.randint(10, 99)
# for i in range(lenX):
#     print(matrix[i])
# result = matrix[0][0] + matrix[0][2]
# print(result)
#
# numberX = 2 - 1
# number1Y = int(input('Введите номер строки матрицы ')) - 1
# number2Y = int(input('Введите номер строки матрицы ')) - 1
# result = matrix[numberX][number1Y] + matrix[numberX][number2Y]
# print(result)

# import random
# lenX = int(input('Введите размер матрицы '))
# lenY = int(input('Введите размер матрицы '))
# matrix = [[]] * lenX
# for i in range(lenX):
#     matrix[i] = [0] * lenY
#     # print(matrix[i])
# for i in range(lenX):
#     for j in range(lenY):
#         matrix[i][j] = random.randint(10, 99)
# for i in range(lenX):
#     print(matrix[i])

# numberX = int(input('Введите строку матрицы '))
# numberY = int(input('Введите столбец матрицы '))
# result = matrix[numberX][numberY]
# print(result)

# result = sum(matrix[2])
# print(result)
# 12.69 а
# result = 0
# if matrix[5][i] % 2 != 0:
#     result = (sum(matrix[5])) / len(matrix)
# print(result)

# import random
# lenX = int(input('Введите размер матрицы '))
# lenY = int(input('Введите размер матрицы '))
# matrix = [[]] * lenX
# for i in range(lenX):
#     matrix[i] = [0] * lenY
#     # print(matrix[i])
# for i in range(lenX):
#     for j in range(lenY):
#         matrix[i][j] = random.randint(10, 99)
# for i in range(lenX):
#     print(matrix[i])

# 12.6 б
# number = int(input('Введите номер строки массива\n'))
# result = matrix[number]
# print(result)

# # 12.5 б
# number = int(input('Введите номер столбца массива\n'))
#
# for i in range(lenX):
#     print(matrix[i][number], end=' ')


# 12.16 а
# number1X = int(input('Введите номер строки массива 1-го элемента \n'))
# number1Y = int(input('Введите номер столбца массива 1-го элемента \n'))
# number2X = int(input('Введите номер строки массива 2-го элемента \n'))
# number2Y = int(input('Введите номер строки массива 2-го элемента \n'))
# result = matrix[number1X][number1Y] - matrix[number2X][number2Y]
# print(result)

# 12.33 a

# matrY = 3
# for item in range(lenX -1, -1, -1):
#     print(matrix[item][matrY])


# 12.62 a
# number = int(input('Введите номер строки массива\n'))
# number1 = int(input('Введите номер строки массива\n'))
# result = sum(matrix[number])
# result1 = sum(matrix[number1])
# print(f'{result}, {result1}')

# 12.90 а,б

# number = int(input('Введите номер строки массива\n'))
# somString = []
# for i in range(len(matrix)):
#     somString.append(min(matrix[i]))
# print(somString)

# result = max(matrix[number])
# result1 = min(matrix[number])
# print(f'минимальное значение в массиве = {result1}, максимальное значение в массиве = {result}')

# progLang = {'python', 'JavaScripts', 'Go'} # коллекция уникальные перевод set
# # print(len(progLang))
# # for lang in progLang:
# #     print(lang)
# # print('python' in progLang) # наличие элемента в коллекции
#
# progLang.add('Java') # добавляем элемент
# # print(progLang)
# secondLang = {'C+', 'C++'}
# print(type(secondLang))
# progLang.update(secondLang) # добавляем secondLang только уникальные
# print(progLang)
# progLang.remove('C++') # удаление если нет ошибка
# print(progLang)
# progLang.discard('Ja') # если нет данных он не удалит т.е. Ja
# # progLang.pop() # удаляет случайно
# # progLang.clear() # удаляет все


# import os
# import function
#
# maxUsers = 5
# users = set()
# os.system('cls')
# print('start')
#
# while True:
#     print('1. Имена пользователей в коворкинге')
#     print('2. Количество пользователей')
#     print('3. Добавьте пользователя')
#     print('4. Удалить пользователя')
#     print('0. Выход из программы')
#     choice = input('Введите порядковый номер: ')
#     if choice == '0':
#         break
#     elif choice == '1':
#         function.print_users(users)
#     elif choice == '2':
#         function.print_count_users(users)
#     elif choice == '3':
#         function.add_users(users, maxUsers)
#     elif choice == '4':
#         function.remove_users(users)
#     else:
#         print('Неправильное действие')
#     print()
#
#     input('Нажмите Enter для продолжения ')
#     os.system('cls')
# print('Конец')

# import os
# garage = [''] * 3
# # maxCountCar =
# while True:
#     print('0. Выход')
#     print('1. Добавить авто')
#     print('2. Удалить авто')
#     print('3. Список авто')
#     print('4. Количество авто')
#     choice = input('Вебирите номер: ')
#     if choice == '0':
#         break
#     elif choice == '1':
#         if garage.count('') == 0:
#             print('Гараж пуст')
#         else:
#             carNumber = input('Введите номер машины: ')
#             print('Список авто ', garage)
#             index = int(input('Введите индекс: '))
#             garage[index] = carNumber
#     elif choice == '2':
#         carNumber = input('Введите номер машины: ')
#         if carNumber in garage:
#             index = int(input('Введите индекс: '))
#             del garage[index]
#         else:
#             print('Номера машины нет в гараже', garage)
#     elif choice == '3':
#         print('Список машин в гараже', garage)
#     elif choice == '4':
#         print('Количество авто в гараже = ',len(garage))


# import datetime
# from datetime import timedelta
# time = datetime.datetime.now()
# date = input('Введите дату\n')
# sutky = int(input('Введите количество суток\n'))
# result = date + timedelta(days=sutky)
# print(result)


# print(date)
# # print(time.date())
# # print(time.now())
# # result = time.strftime('%d.%m.%Y|%H:%M:%S')
# # result = time.strftime('%Y.%m.%d|%H:%M:%S')
# print(result)
# date = date.replace('+','').replace(' ','')
# print(date)
# *numbers - неограниченное кол-во параметров

def template_first(name_shop):
    return lambda number, name_product: f'{name_shop}: Serial - {number}; Name - {name_product}'

l_1 = template_first('Shop_1')
result = l_1(4567, 'Category')
print(result)
