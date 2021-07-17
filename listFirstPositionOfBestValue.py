# find the position of the first best value

numbers = [100, 2, 1000,1000, 3, 4, 1000, 1, 4, 4, 55, 1000]
best_position = 0

for position in range(1, len(numbers)):
    if numbers[position] > numbers[best_position]:
        best_position = position

print(best_position)
