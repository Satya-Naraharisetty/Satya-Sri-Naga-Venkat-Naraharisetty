def series_of_numbers(count):
    # series = []
    # for i in range(count):
    #     num = 2 * i + 1
    #     series.append(str(num))

    return [str(2 * i + 1) for i in range(count)]

if __name__ == "__main__":
    try:
        a = int(input("Enter a: "))
        count = (a + 1) // 2
        print(", ".join(series_of_numbers(count)))
    except Exception as e:
        print("Error:", e)