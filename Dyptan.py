import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

'''setA = []
setB = []
element_number = []

print("Введите количество элементов в массиве A и массиве B")
for i in range(int(input())): 
    element_number.append(int(i)) 

print("Введите значения " + str(len(element_number)) + " элементов массива A")
for i in range(len(element_number)): 
    setA.append(float(input())) 

print("Введите значения " + str(len(element_number)) + " элементов массива B")
for i in range(len(element_number)): 
    setB.append(float(input())) 
'''
setA = [18, 20.5, 6.5, 8.4, 13, 14, 3.85]
setB = [47, 15, 20, 15,9, 7.5, 11]
element_number=[1, 2, 3, 4, 5, 6, 7]

minA = min(setA)
maxA = max(setA)
minB = min(setB)
maxB = max(setB)

def WorkSetA(setName, miin, maax):
    List = []
    for x in setName:
        if x <= miin:
            List.append(0)
        elif x >= maax:
            List.append(1)
        else:
            z=(x-miin)/(maax-miin)
            List.append(round(z,2))  #округление до двух цифр после запятой
    return List

def WorkSetB(setName, miin, maax):
    List = []
    for x in setName:
        if x<= miin:
            List.append(1)
        elif x >= maax:
            List.append(0)
        else:
            z = (maax-x)/(maax-miin)
            List.append(round(z,2))
    return List

def Dopolnenie (WorkSet):
    List = []
    for x in WorkSet:
        z = x - 1
        List.append(abs(round(z,2)))
    return List

def Maax (element_numbersA, element_numbersB):
    List=[]
    for x in range(0, len(element_number)):
        if element_numbersA[x]>=element_numbersB[x]:
            List.append(element_numbersA[x])
        else:
            List.append(element_numbersB[x])
    return List

def Miin (element_numbersA, element_numbersB):
    List=[]
    for x in range(0, len(element_number)):
        if element_numbersA[x]<=element_numbersB[x]:
            List.append(element_numbersA[x])
        else:
            List.append(element_numbersB[x])
    return List

def CON(element_numbers):
    List = []
    for x in element_numbers:
        z = x**2
        List.append(z)
    return List

def DIL(element_numbers):
    List = []
    for x in element_numbers:
        z = x**0.5
        List.append(z)
    return List

formulaA= list(WorkSetA(setA, minA, maxA))
formulaB= list(WorkSetB(setB, minB, maxB))
DopolnenieA = Dopolnenie(formulaA) 
DopolnenieB = Dopolnenie(formulaB) 
unification= Maax(formulaA,formulaB) 
intersection= Miin(formulaA,formulaB) 
AminusB=Miin(formulaA, DopolnenieB) 
BminusA=Miin(formulaB, DopolnenieA) 
conA=CON(formulaA) 
conB=CON(formulaB) 
dilA=DIL(formulaA) 
dilB=DIL(formulaB) 

fig, axs = plt.subplots(nrows= 4 , ncols= 2) #создание рисунока с сеткой графиков 4*2

axs[0][0].plot(element_number, formulaA, label = 'Множество А')
axs[0][0].plot(element_number, DopolnenieA, label = 'Дополение А')
axs[0][0].legend()

axs[0][1].plot(element_number, formulaB, label = 'Множество B')
axs[0][1].plot(element_number, DopolnenieB, label = 'Дополение B')
axs[0][1].legend()

axs[1][0].plot(element_number, formulaA, label = 'Множество А')
axs[1][0].plot(element_number, formulaB, label = 'Множество B')
axs[1][0].plot(element_number, intersection, label = 'Объединение')
axs[1][0].legend()

axs[1][1].plot(element_number, formulaA, label = 'Множество А')
axs[1][1].plot(element_number, formulaB, label = 'Множество B')
axs[1][1].plot(element_number, unification, label = 'Пересечение')
axs[1][1].legend()

axs[2][0].plot(element_number, formulaA, label = 'Множество A')
axs[2][0].plot(element_number, formulaB, label = 'Множество B')
axs[2][0].plot(element_number, AminusB, label = 'А - В')
axs[2][0].legend()

axs[2][1].plot(element_number, formulaA, label = 'Множество А')
axs[2][1].plot(element_number, formulaB, label = 'Множество B')
axs[2][1].plot(element_number, BminusA, label = 'В - А')
axs[2][1].legend()

axs[3][0].plot(element_number, formulaA, label = 'Множество А')
axs[3][0].plot(element_number, conA, label = 'Концентрация множества A')
axs[3][0].plot(element_number, dilA, label = 'Растяжение множества A')
axs[3][0].legend()

axs[3][1].plot(element_number, formulaB, label = 'Множество B')
axs[3][1].plot(element_number,conB, label = 'Концентрация множества B')
axs[3][1].plot(element_number,dilB, label = 'Растяжение множества B')
axs[3][1].legend()

plt.show()

def Chetkoe(WorkSet):
    List = []
    for x in WorkSet:
        if x < 0.5:
            List.append(0)
        elif x >= 0.5:
            List.append(1)
    return List

def Hemming(mn1, mn2):
    result = 0
    for i in range(0, len(element_number)):
        result += abs(mn1[i] - mn2[i])
    return result

def Evklidivo(mn1, mn2):
    result = 0
    for i in range(0, len(element_number)):
        result += (mn1[i] - mn2[i])**2
    result = result**0.5
    return result

def a_crez(mn, a):
    List = []
    for i in range(0, len(element_number)):
        if mn[i] >= a:
            List.append(element_number[i])
    return List

ChetkoeA = Chetkoe(formulaA)
ChetkoeB = Chetkoe(formulaB)

print ("Расстояние Хемминга = " + str(Hemming(formulaA, formulaB)))
print ("Относительное расстояние Хемминга = " + str(Hemming(formulaA, formulaB)/len(element_number)))
print ("Евклидово(квадратичное) расстояние = " + str(Evklidivo(formulaA, formulaB)))
print ("Относительное Евклидово(квадратичное) расстояние = " + str(Evklidivo(formulaA, formulaB)/(len(element_number)**0.5)))
print ("Линейный индекс нечеткости для множества A = " + str(2*Hemming(formulaA, ChetkoeA)/len(element_number)))
print ("Линейный индекс нечеткости для множества B = " + str(2*Hemming(formulaB, ChetkoeB)/len(element_number)))
print ("Квадратичный индекс нечеткости для множества A = " + str((2*Evklidivo(formulaA, ChetkoeA))/(len(element_number)**0.5)))
print ("Квадратичный индекс нечеткости для множества B = " + str((2*Evklidivo(formulaB, ChetkoeB))/(len(element_number)**0.5)))
print ("Мера нечеткости Егера 1 для множества A = " + str(1-(Hemming(formulaA, DopolnenieA)/len(element_number))))
print ("Мера нечеткости Егера 1 для множества B = " + str(1-(Hemming(formulaB, DopolnenieB)/len(element_number))))
print ("Мера нечеткости Егера 2 для множества A = " + str(1-(Evklidivo(formulaA, DopolnenieA)/len(element_number)**0.5)))
print ("Мера нечеткости Егера 2 для множества B = " + str(1-(Evklidivo(formulaB, DopolnenieB)/len(element_number)**0.5)))
print ("Кардинальное число для множества A = " + str(sum(formulaA)))
print ("Кардинальное число для множества B = " + str(sum(formulaB)))
print ("Мера нечеткости Коско для множества A = " + str(sum(Miin(formulaA,DopolnenieA))/sum(Maax(formulaA,DopolnenieA))))
print ("Мера нечеткости Коско для множества B = " + str(sum(Miin(formulaB,DopolnenieB))/sum(Maax(formulaB,DopolnenieB))))

print("Введите значение a: ")
a = float(input())
print("Введите множество, а-срез которого вы хотите узнать")
mn = input()

if (mn == "A" or mn == "a" or mn == "А" or mn == "а"):
    print ("Значение a-среза для множества " + str(mn) + " = " + str(a_crez(formulaA, a)))
if (mn == "B" or mn == "b" or mn == "В" ):
    print ("Значение a-среза для множества " + str(mn) + " = " + str(a_crez(formulaB, a)))