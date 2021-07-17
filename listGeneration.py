# list generation

counter = 0
list = []
stop_loop = False

while stop_loop == False:
    list = list + [counter]
    counter = counter + 1
    
    if counter > 9:
        stop_loop = True
    
print(list)
