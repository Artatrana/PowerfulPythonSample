# Write python program to move all the zero to the start of the list
# by keeping intact the non-zeor value order
# Example [3,23, 0, 14,0, 8, 74,0, 64,0] would be [0,0,0, 0,3,23,14,8,74,64]

def move_zero_to_start(lst: list) -> list:
    non_zero_lst = [i for i in lst if i!=0]
    return [0] * (len(lst)-len(non_zero_lst)) + non_zero_lst 
        
#print(move_zero_to_start([3,23, 0, 14,0, 8, 74,0, 64,0] ))
#print(move_zero_to_start([6,35,0, 0,3,23,32] ))

def move_zero_to_start1(lst: list) -> list:
    insert_position = len(lst) -1 

    for i in range(len(lst), -1, -1):
        if lst[i] !=0:
            lst[insert_position] = lst[i]
            insert_position += 1
    
    for i in range(insert_position + 1):
        lst[i]

    return lst 

print(move_zero_to_start([3,23, 0, 14,0, 8, 74,0, 64,0] ))
print(move_zero_to_start([6,35,0, 0,3,23,32] ))
print(move_zero_to_start([0, 0,3,23,32,0] ))
print(move_zero_to_start([3,23,32,0,0,0] ))
print(move_zero_to_start([0] ))
print(move_zero_to_start([1,0,0] ))
