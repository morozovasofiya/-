# Функции

def ReadText(p):  # запись условий задач в список
    s_task = []
    for i in range(0, type):
        begin = p.find('TYPE = ' + str(i))
        end = p.find('TYPE = ' + str(i + 1))
        srez = p[begin + 9:end]
        s_task.append(srez)
    return s_task
   # print(s_task, end=' ')

def PrintTask(task,i):  # функция выводит условие с числовыми данными
    pos_f = task.find('first')
    pos_s = task.find('second')
    pos_1 = task.find(']')
    pos_2 = task.rfind(']')
    print(task[0:pos_f] + str(s_first[i])  +  str(s_second[i]))

def GenerFirst(task): #генерируем список для первой переменной отправляю s_task
    pos1 = task.find('[')
    pos2 = task.find(']')
    srez1 = task[pos1 + 1:pos2]
    num1, num2 = srez1.split()
    a = int(num1)
    b = int(num2)
    return random.randint(a, b + 1)

def GenerSecond(task): #генерируем значения переменных
    pos3 = task.rfind('[')
    pos4 = task.rfind(']')
    srez1 = task[pos3 + 1:pos4]
    num3, num4 = srez1.split()
    a = int(num 4)
    b = int(num 3)
    return random.randint(a, b + 1)


def GenerSi1(task, spisok, c): #генерируем единицы измерения
    pos3 = task.find('(')
    pos4 = task.find(')')
    srez1 = task[pos3 + 1:pos4]
    k = str(srez1)
    if k == 'кг':
        spisok = ['г', 'кг']
        a = len(spisok)
        c = random.randint(0, a - 1)
    elif k == 'H':
        spisok = ['кН', 'МН', 'Н']
        a = len(spisok)
        c = random.randint(0, a - 1)
    elif k == 'км':
        spisok = ['м', 'км']
        a = len(spisok)
        c = random.randint(0, a - 1)
    return spisok[c]


def GenerSi2(task, spisok, c): #генерируем единицы измерения
    pos3 = task.rfind('(')
    pos4 = task.rfind(')')
    srez1 = task[pos3 + 1:pos4]
    k = str(srez1)
    if k == 'кДж':
        spisok = ['Дж', 'МДж', 'кДж']
        a = len(spisok)
        c = random.randint(0, a - 1)
    elif k == 'см':
        spisok = ['см', 'км']
        a = len(spisok)
        c = random.randint(0, a - 1)
    elif k == 'м':
        spisok = ['м', 'км']
        a = len(spisok)
        c = random.randint(0, a - 1)
    return spisok[c]



def Quest(i):
    task = s_task[i]
    PrintTask(task,i)
    print("Ваш ответ: ")
    ans = input()
    if i == 0:
        if int(ans) == Task_0(s_first[i], s_second[i]):
            print("Ответ верный")
        else:
            print("Ответ неверный, правильный ответ: ", Task_0(s_first[i], s_second[i]))
    elif i == 1:
        if float(ans) == Task_1(s_first[i], s_second[i]):
            print("Ответ верный")
        else:
            print("Ответ неверный, правильный ответ: ", Task_1(s_first[i], s_second[i]))
    else:
        if float(ans) == Task_2(s_first[i], s_second[i]):
            print("Ответ верный")
        else:
            print("Ответ неверный, правильный ответ: ", Task_2(s_first[i], s_second[i]))

def Task_0(m, h):
    return m * h * 10

def Task_1(m, h):
    return m * h / 100

def Task_2(m, h):
    return (h * 10**3) / (m * 10**3)

###############################################
# Main
import random
f = open('1.txt','r')
p = f.read()


type = int(p[-1])
s_task = [''] * type
s_task = ReadText(p)
s_first = [''] * type
s_second = [''] * type
spisok = [''] * type
c = 0
s_si1 = [''] * type
s_si2 = [''] * type
for i in range (0, type):
    s_first[i] = GenerFirst(s_task[i])
    s_second[i] = GenerSecond(s_task[i])
    Quest(i)
f.close()
###############################################
