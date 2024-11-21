def square(x):
    return x*x


x = float(input("Введите сторону квадрата (допустима десятичная дробь): "))

s = square(x)

if s % 1 == 0:
    print("Площадь квадрата:", s)
else:
    print("Площадь квадрата:", s - s % 1 + 1)
