numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers1 = [x for x in numbers if x % 2 == 0]
print(numbers1)

numbers1 = [x for x in numbers1 if x > 5]
print(numbers1)

print(7 in numbers)