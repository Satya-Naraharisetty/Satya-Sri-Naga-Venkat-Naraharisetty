a = int(input("Enter a: "))

count = (a + 1) // 2
series = []
for i in range(count):
    num = 2 * i + 1
    series.append(str(num))

print(", ".join(series))