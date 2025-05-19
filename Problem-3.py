a = int(input("Enter a: "))

series = []
for i in range(a):
    num = 2 * i + 1
    # Only add numbers less than or equal to 2*a - 1 and less than 10
    if num < 10:
        series.append(str(num))
    else:
        break

print(", ".join(series))