# List transformation

a_list = [2, 5, 1]
list_length = len(a_list)

for list in range(0, list_length):
    
   # transform the last index in the list
   if list == list_length -1 and a_list[list] == 1:
       a_list[list] = 0
print(a_list)
