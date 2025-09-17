n = int(input("Введіть n:"))
while n <= 1 or n >= 10:
    n = int(input("Введіть ще раз n: "))

for i in range(1, n + 1):
    num = n
    for j in range(0, n, 1):
        if j >= i:
            print(" ", end = " ")
        else:
            print(num, end = " ")
            num -= 1
    print("")