a = int(input ("Введіть а: "))

while (a <= 0):
    a = int(input ("Введіть а: "))

b = int(input ("Введіть b: "))

while (b <= 0):
    b = int(input ("Введіть ще раз b: "))

if a < b:
    r = a / b - 1
elif a == b:
    r = -25
else:
    r = (a**3 - 5) / a

print("Відповідь: " , r)