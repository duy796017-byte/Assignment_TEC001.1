def remove_odd(lst):
    return [x for x in lst if x % 2 == 0]
numbers = [1, 2, 3, 4, 5, 6, 7]
filtered = remove_odd(numbers)
print("List gốc:", numbers)
print("List sau khi lọc:", filtered)