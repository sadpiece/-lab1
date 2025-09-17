print("Годин", " ", "ударів")
bangs = 0
for time in range(0, 16, 1):
    print(time, " " * 4, time)
    bangs += time

print("всього ударів за даний період", bangs)