def numberSummator(megaStroka):
    a = 0
    for i in megaStroka:
        a += int(i)
    print("Сумма строки равна: " + str(a))
    return


b = input("Введите число для сумирования его циферок: ")
numberSummator(b)