import random
import sys


def delete(mass):  # функция нахождения самой длинной цепочки четных элементов
    mas_i = []
    mas2 = []
    mass3 = []  # массив для окончательного результата
    for i in range(0, len(mass)):
        if mass[i] % 2 == 0:
            mas2.append(i)
            if len(mas2) > len(mas_i):  # проверка на длинну цепочек (нахождение самой длинной)
                mas_i = mas2
        else:
            mas2 = []
    for i in range(mas_i[0], mas_i[-1] + 1):  # если цепочка самая длинная, то символы заменяются
        mass[i] = "&"
    for Z in range(0, len(mass)):
        if mass[Z] != "&": # удаление цепочки
            mass3.append(mass[Z])
    print("Результат: ", mass3)


while True:
    a = int(input("Введите 0 для ручной реализации или 1 для автоматической: "))
    mas = []
    mas3 = []
    if a == 1:
        mas = [random.randint(0, 100) for i in range(random.randint(3, 8))]
        print("Исходный массив: ", mas)
        delete(mas)
    elif a == 0:
        count = int(input("Введите количество элементов: "))
        for i in range(count):
            print("Введите число")
            mas.append(int(input()))
        print("Исходный: ", mas)
        delete(mas)
    else:
        print("error")
    sys.exit()
