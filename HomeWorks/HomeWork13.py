import ArrayFunctions
def arrayComparator(firstArray, secontArray):
    resultArray = []
    for i in firstArray:
        for j in secontArray:
            if i == j and resultArray.count(i) == 0:
                resultArray.append(i)
    resultArray.sort()
    print(resultArray)
    return


a = ArrayFunctions.ruletka(0, 9, 10)
b = ArrayFunctions.ruletka(0, 9, 10)
print("Первый случайный массив")
print(a)
print("Второй случайный массив")
print(b)
print("Общее в массивах")
arrayComparator(a, b)
