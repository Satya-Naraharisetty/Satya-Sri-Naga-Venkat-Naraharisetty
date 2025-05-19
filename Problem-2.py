def series_of_odd_numbers(n):
    # series = []
    # for i in range(n):
    #     num = 2 * i + 1
    #     series.append(num)
    # return series
    return [str(2 * i + 1) for i in range(n)]

if __name__ == "__main__":
    try:
        a = int(input("Enter a: "))
        print(", ".join(series_of_odd_numbers(a)))
    except Exception as e:
        print("Error:", e)