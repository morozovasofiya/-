#Модуль учителя
#############################################################
# Функции
def insert(pos, string, pstring):
  str1 = string[:pos + 1]
  str2 = string[pos + 2:]
  f_string = str1 + ' ' + pstring + ' ' + str2
  return f_string
#вставка подстроки в строку

def EnterTask():
    print('Введите текст задачи: ')
    text = input()  # текст задачи
    print('Напишите, что в Вашей задаче является первой переменной: ', end='')
    first = input()
    first1 = ' ' + first + ' '
    text = text.replace(first1, ' first ')
    pos = text.find('t')
    print('Введите диапозон для генерации первой переменной в СИ (ввод через пробел): ', end='')
    x1 = input()
    x1 = '[' + x1 + ']'
    text = insert(pos, text, x1)
    print('Напишите, что является единицей измерения: ', end = '')
    s_si1 = input()  # строка
    s_si = '] ' + s_si1
    text = text.replace(s_si, '] ' + '<' + s_si1 + '>')
    print('Напишите, что в Вашей задаче является второй переменной: ', end='')
    second = input()
    second1 = ' ' + second + ' '
    text = text.replace(second1, ' second ')
    pos = text.find('d')
    print('Введите диапозон для генерации второй переменной в СИ (ввод через пробел): ', end='')
    x2 = input()
    x2 = '[' + x2 + ']'
    text = insert(pos, text, x2)
    print('Напишите, что является единицей измерения: ', end = '')
    s_si2 = input()
    s_si = '] ' + s_si2
    text = text.replace(s_si, '] ' + '<' + s_si2 + '>')
    print('Введите фомулу для решения задачи: ', end ='')
    formula = input()
    formula = formula.replace(first, 'first')
    formula = formula.replace(second, 'second')
    text = text + ' ' + '{' + formula + '}'
    print('Текст условия задачи с разметкой:',text)
    return text

#Модуль ученика
#############################################################
# Функции
def ReadText(p):
    s_task = []
    for i in range(0, type):
        begin = p.find('TYPE = ' + str(i))
        end = p.find('TYPE = ' + str(i + 1))
        srez = p[begin + 9:end]
        s_task.append(srez)
    return s_task
# запись условий задач в список

def GenerFirst(task):
    pos1 = task.find('[')
    pos2 = task.find(']')
    srez1 = task[pos1 + 1:pos2]
    num1, num2 = srez1.split()
    a = int(num1)
    b = int(num2)
    ref_t = random.randint(a, b + 1)
    return ref_t
#генерируем список для первой переменной отправляю s_task

def GenerSecond(task):
    pos3 = task.rfind('[')
    pos4 = task.rfind(']')
    srez1 = task[pos3 + 1:pos4]
    num3, num4 = srez1.split()
    a = int(num3)
    b = int(num4)
    return random.randint(a, b + 1)
#генерируем список для второй переменной отправляю s_task

def GenerSi1(task): #генерируем единицы измерения
    pos3 = task.find('<')
    pos4 = task.find('>')
    srez1 = task[pos3 + 1:pos4]
    k = str(srez1)
    return Izmerenie(k)
#генерируем список единицы измерения первой переменной

def GenerSi2(task):
    pos1 = task.rfind('<')
    pos2 = task.rfind('>')
    srez1 = task[pos1 + 1:pos2]
    k = str(srez1)
    return Izmerenie(k)
#генерируем список единицы измерения второй переменной

def Izmerenie(k):
    spisok = [' ']
    c = ''
    if k == 'Дж':
        spisok = ['Дж', 'МДж', 'кДж']
        a = len(spisok)
        c = spisok[random.randint(0, a - 1)]
        return c
    elif k == 'м':
        spisok = ['см', 'м', 'км']
        a = len(spisok)
        c = spisok[random.randint(0, a - 1)]
        return c
    elif k == 'Н':
        spisok = ['Н', 'КН']
        a = len(spisok)
        c = spisok[random.randint(0, a - 1)]
        return c
    elif k == 'кг':
        spisok = ['г', 'кг']
        a = len(spisok)
        c = spisok[random.randint(0, a - 1)]
        return c
#выбор единиц измерения для генерации

def SiSystem(number, si):
    if si == 'г':
        number = number * 10 ** (-3)
    elif si == 'кг':
        number = number
    elif si == 'КН':
        number = number * 10 ** (-3)
    elif si == 'Н':
        number = number
    elif si == 'Дж':
        number = number
    elif si == 'кДж':
        number = number * 10 ** -3
    elif si == 'мДж':
        number = number * 10 * -6
    elif si == 'км':
        number = number * 10 ** (-3)
    elif si == 'см':
        number = number * 100
    elif si == 'м':
        number = number
    return number
#перевод числа в какую-то единицу измерения

def ReadFormula(task):
    pos_1 = task.find('{')
    pos_2 = task.find('}')
    srez = task[pos_1 + 1:pos_2]
    return srez
#считывание формулы

def CountAnswer(task):
    first = s_first[i]
    second = s_second[i]
    s = ReadFormula(task)
    s1 = str(s)
    return eval(s1)
#получение ответа

def Quest(i):
    task = s_task[i]
    flag = False
    while (flag == False):
        print("Ваш ответ: ", end  = '')
        try:
            ans = input()
            Answer = CountAnswer(task)
            if float(ans) == Answer:
                print("Ответ верный")
            else:
                print("Ответ неверный, правильный ответ: ", end = '')
                print("%.3f" % Answer)
            flag = True
        except ValueError:
            print('Ответ содержит посторонние знаки')

###############################################
# Main
import random
from colorama import init
from termcolor import colored
#################Вставка подстроки в строку

################################
fl = False
print('''С каким модулем Вы хотите работать?
    1. Решение задач
    2. Добавление задач''')
while fl == False:
    print('Выберите 1 или 2:')
    try:
        a = int(input())
        fl = True
    except ValueError:
        print('Требуется выбрать 1 или 2')
f = open('1.txt', mode = 'r', encoding = 'utf-8')
p = f.read()
type = int(p[-1])
if a == 1:
    s_task = [''] * type
    s_task = ReadText(p)
    s_first = [''] * type
    s_second = [''] * type
    s_si1 = [''] * type
    s_si2 = [''] * type
    for i in range(0, type):
        s_first[i] = GenerFirst(s_task[i])
        s_second[i] = GenerSecond(s_task[i])
        s_si1[i] = GenerSi1(s_task[i])
        s_si2[i] = GenerSi2(s_task[i])
        # собирается текст задачи на экране
        pos_f = s_task[i].find('first')
        pos_s = s_task[i].find('second')
        pos_4 = s_task[i].find('>')
        pos_6 = s_task[i].rfind('>')
        pos_7 = s_task[i].find('{')
        first = SiSystem(s_first[i], s_si1[i])
        #print(s_first[i], s_si1[i], first)
        second = SiSystem(s_second[i], s_si2[i])
        #print(s_second[i], s_si2[i], second)
        print(colored(s_task[i][0:pos_f] + str(first) + ' ' + str(s_si1[i]) + s_task[i][pos_4 + 1:pos_s] + str(second) + ' ' + str(
            s_si2[i]) + s_task[i][pos_6 + 1:pos_7], 'blue'))
        ####################################
        Quest(i)
    f.close()
    ###############################################
else:
  type = type + 1
  f.close()
  f = open('1.txt', mode = 'a', encoding = 'utf-8')
  text = EnterTask()
  f.write('\n' + str(text) + '\n')
  f.write('TYPE = ' + str(type))
  f.close()
f.close()
###############################################################################
# f = open('1.txt','r')
# p = f.read()
# type = int(p[-1])
# s_task = [''] * type
# s_task = ReadText(p)
# s_first = [''] * type
# s_second = [''] * type
# s_si1 = [''] * type
# s_si2 = [''] * type
# for i in range (0, type):
#     s_first[i] = GenerFirst(s_task[i])
#     s_second[i] = GenerSecond(s_task[i])
#     s_si1[i] = GenerSi1(s_task[i])
#     s_si2[i] = GenerSi2(s_task[i])
# #собирается текст задачи на экране
#     pos_f = s_task[i].find('first')
#     pos_s = s_task[i].find('second')
#     pos_4 = s_task[i].find('>')
#     pos_6 = s_task[i].rfind('>')
#     pos_7 = s_task[i].find('{')
#     first = SiSystem(s_first[i], s_si1[i])
#     print(s_first[i], s_si1[i],first)
#     second = SiSystem(s_second[i], s_si2[i])
#     print(s_second[i], s_si2[i],second)
#     print(colored(s_task[i][0:pos_f] + str("%.3f" % first) + ' ' + str(s_si1[i]) + s_task[i][pos_4 + 1:pos_s] + str("%.3f" % second) + ' ' + str(
#         s_si2[i]) + s_task[i][pos_6 + 1:pos_7], 'blue'))
# ####################################
#     Quest(i)
# f.close()
# ###############################################
