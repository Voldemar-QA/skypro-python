x = float(input("Сумма вклада, у.е.: "))
y = int(input("Срок вклада, лет: "))


def bank(x, y):
    sum = x
    for y in range(y):
        sum = sum * 1.1

    print("Сумма на счету к концу срока, у.е.:", round(sum, 2))


bank(x, y)
