import random
def ruletka(down, up, elements):
    s = []
    for i in range(elements):
        b = random.randint(down, up)
        s.append(b)
    return s


def findInRuletka(number, ruletkaa):
    a = ruletkaa.count(number)
    if a == 0:
        print("Циферка не найдена")
        return
    b = 0
    for i in range(a):
        print("Циферка найдена под индексом: " + str(ruletkaa.index(number) + b))
        ruletkaa.remove(number)
        b = b + 1
    return
