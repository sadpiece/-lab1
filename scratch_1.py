a = int(input ("Введіть а > 0: "))

while (a <= 0):
    a = int(input ("Введіть ще раз а: "))

b = int(input ("Введіть b > 0: "))

while (b <= 0):
    b = int(input ("Введіть ще раз b: "))

if a < b:
    X = a / b - 1
elif a == b:
    X = -25
else:
    X = (a**3 - 5) / a

print("Відповідь: X = " , X)