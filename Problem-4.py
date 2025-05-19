def count_multiples(numbers):
    multiples_count = {i: 0 for i in range(1, 10)}
    for num in numbers:
        for i in range(1, 10):
            if num % i == 0:
                multiples_count[i] += 1
    return multiples_count

# Example usage:
input_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
output_dict = count_multiples(input_list)
print(output_dict)