import numpy as np # імпорт функцій
import random
import timeit


def bbuble_sort(mylist): # сортування бульбашкою
    exchange = 0 # щотчик обмінів
    count = 0 # щотчик порівнянь
    last_item = len(mylist) - 1
    for i in range(0, last_item): # прохід по спискам
        for x in range(0, last_item): # прохід по спискам
            count += 1
            if mylist[x] > mylist[x + 1]:
                mylist[x], mylist[x + 1] = mylist[x + 1], mylist[x]
                exchange += 1
    print("Число порівнянь:", count) #вивід даних
    print("Число обмінів:", exchange) #вивід даних
    print(" ")

    return mylist


def sel_sort(array): #сортування вибором
    exchange = 0 # щотчик обмінів
    coun = 0 # щотчик порівнянь
    for i in range(len(array) - 1):  #прохід по спискам
        coun += 1
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j = j + 1
        array[i], array[m] = array[m], array[i]
        exchange += 1
    print("Число порівнянь:", coun) #вивід даних
    print("Чсло обмінів:", exchange) #вивід даних
    return array


def insertion(data): # сортування вставками
    exchange = 0 # щотчик обмінів
    count = 0 # щотчик порівнянь
    for i in range(len(data)): #прохід по спискам
        count += 1
        j = i - 1
        key = data[i]
        while data[j] > key and j >= 0:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        exchange += 1
    print("Число порівнянь:", count - 1) #вивід даних
    print("Число обмінів:", exchange) #вивід даних
    return data


while True: # перевірки на правельність ведення
    while True:
        try:
            choose = int(input("bubble sort - 1,selection sort - 2,insertion sort - 3,ваш вибір: ")) #вибір сортування
            if choose <= 3: # якшо вели число 3 і менше цикл зупиняється
                break
            else:
                choose = int(input("bubble sort - 1,selection sort - 2,insertion sort - 3,ваш вибір: "))
        except ValueError: # якщо весит букву видасть "тільки цифри"
            print("Тільки цифри")
    flag = input(
        "Якщо ви хочите рандомні вихідні данні, натисніть «Enter». Для введення вручну натисніть любу другу клавішу: ")
    print("")
    if flag == "":
        while True:
            try:
                b = int(input("Введіть кількість яка буде генеруватися: ")) # введеня даних
                break
            except ValueError:
                print("Тільки цифри")

        a = np.zeros(b, dtype=int)
        while True:
            try:
                d1 = int(input('Ліва грань: ')) # введеня даних
                d2 = int(input('Права грань: ')) # введеня даних
                break
            except ValueError:
                print("Тільки цифри")
        if d1 > d2: #якщо вести некоректно границі програма їх поміняє
            buf = d1
            d1 = d2
            d2 = buf
        print("Ви вели не коректоно границі ми їх поміняли для того щоб програма працювала", d1, d2)

        for i in range(b):
            a[i] = random.randint(d1, d2)

    else:
        while True:# перевірка на правельність введення
            try:
                b = int(input("Введіть кількість яка буде генеруватися: ")) # ведення даних
                if b <= 30:
                    break
                else:
                    b = int(input("Введіть кількість яка буде генеруватися: ")) # ведення даних
            except ValueError:
                print("Тільки цифри")
        a = np.zeros(b, dtype=int)
        for i in range(b):
            a[i] = int(input(f'Enter {i + 1} element: '))

    if choose == 1: # якщо вибрали бульбашковий вид сортування
        print("Старий список", a)
        print(" ")
        new = bbuble_sort(a)
        print("Відсортований від меншого до більшого", new)
        print(" ")
        s = np.array(a)
        x = s[::-1]
        print("Від більшого до меншого", x)
        print(" ")
    if choose == 2:# якщо вибрали сортування вибором
        print("Старий список", a)
        print(" ")
        new = sel_sort(a)
        print("Відсортований від меншого до більшого", new)
        print(" ")
        s = np.array(a)
        x = s[::-1]
        print("Від більшого до меншого", x)
        print(" ")
    if choose == 3:# якщо вибрали сортування вставками
        print("Старий список", a)
        print(" ")
        new = insertion(a)
        print("Відсортований від меншого до більшого", new)
        print(" ")
        s = np.array(a)
        x = s[::-1]
        print("Від більшого до меншого", x)
        print(" ")
    t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000) #таймер скільки виконувалась програма
    print(f"Програма виконувалася {t} секунд")
    print(" ")
    if input('Нажмите "Enter" (введите пусту строку (\'\')) для перезапуска: ') == '': #перезапуск програми
        continue
    break