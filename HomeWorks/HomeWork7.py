def nevagno(a, b, c):
    while a < b:
        a += c
    print("Наконец A упало с трубы так как B стало тяжелее, жизненный итог мега важное число: " + str(a))
    return


aa = int(input("Введи мега важное число которое будем увеличивать: "))
bb = int(input("Введи грань на которорой программа завершиться: "))
cc = int(input("Введи великий уравнитель: "))

nevagno(aa, bb, cc)

