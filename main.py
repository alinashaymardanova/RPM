import math

if __name__ == "__main__":
    a = int(input("a="))
    b = int(input("b="))
    c = int(input("c="))
    D = ((b ^ 2) - 4 * a * c)
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print(x1, x2)
    elif D == 0:
        x = -b / (2 * a)
        print(x)
    else:
        print("Нет корней")
