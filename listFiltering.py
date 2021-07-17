# list filtering

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 4
filtered_list = []

for number in numbers:
    if number > target_value:
        filtered_list = filtered_list + [number]
        
print(filtered_list)
