a = int(input("Enter a: "))

# series = []
# for i in range(a):
#     series.append(str(2 * i + 1))

series = [str(2 * i + 1) for i in range(a)]

print(", ".join(series))