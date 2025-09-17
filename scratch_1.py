a = int(input ("Введіть а: "))

while (a <= 0):
    a = int(input ("Введіть а: "))

b = int(input ("Введіть b: "))

while (b <= 0):
    b = int(input ("Введіть ще раз b: "))

if a < b:
    X = a / b - 1
elif a == b:
    X = -25
else:
    X = (a**3 - 5) / a

print("Відповідь: X = " , X)