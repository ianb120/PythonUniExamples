# Find the highest value
a_list = [2, 5, 1, 2, 4, 5, 6, 7, 200]
list_length = len(a_list)
list_comparision = a_list[0]

for list in range(1, list_length):
    if a_list[list] > list_comparision:
        list_comparision = a_list[list]
        
print(list_comparision)
