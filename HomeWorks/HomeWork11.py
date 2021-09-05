import ArrayFunctions
def superChanger(initialList, changeItemIndex, changeToValue):
    a = initialList[changeItemIndex]
    initialList[changeItemIndex] = changeToValue
    print(str(a) + " из списка заменяется на " + str(changeToValue))
    return


b = ArrayFunctions.ruletka(0, 9, 10)
print(b)
c = int(input("Введите номер елемента для замены: "))
d = int(input("Введите значение на которгое нужно заменить елемент: "))
superChanger(b, c, d)
print(b)