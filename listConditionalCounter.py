# list counter

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
counter = 0

for num in numbers:
    if num > 5:
        counter = counter + 1

print('numbers more than five in the list are', counter)
