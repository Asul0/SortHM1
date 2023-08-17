def counting_sort(arr):
    min_val = min(arr)
    max_val = max(arr)
    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements
    output = [0] * len(arr)

    for num in arr:
        count[num - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output

# Пример использования
arr = [4, -2, -9, 5, 4, -6, 7, 0, -1]
sorted_arr = counting_sort(arr)
print("Отсортированный массив:", sorted_arr)
