N = int(input("Введіть N:"))
while N <= 1 or N >= 9:
    n = int(input("Введіть ще раз N: "))

for i in range(1, N + 1):
    num = N
    for j in range(0, N, 1):
        if j >= i:
            print(" ", end = " ")
        else:
            print(num, end = " ")
            num -= 1
    print("")