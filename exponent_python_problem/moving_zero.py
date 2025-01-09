# Write python program to move all the zero to the end of the list
# by keeping intact the non-zeor value order
# Example [3,23, 0, 14,0, 8, 74,0, 64,0] would be [3,23,14,8,74,64, 0,0,0, 0]

def move_zero_to_end(lst: list) -> list:
    lst_len = len(lst)
    counter = 0
    for ind, value in enumerate(lst):
        if value != 0:
            lst[counter] = value
            counter += 1
    while counter < lst_len:
        lst[counter] = 0
        counter += 1
    return lst
        

#print(move_zero_to_end([3,23, 0, 14,0, 8, 74,0, 64,0] ))
#print(move_zero_to_end([ 0, 0,3,23,32] ))


def move_zero_to_end1(lst: list) -> list:
    non_zero_lst = [i for i in lst if i!=0]
    return non_zero_lst + [0] * (len(lst)-len(non_zero_lst)) 
        

#print(move_zero_to_end([3,23, 0, 14,0, 8, 74,0, 64,0] ))
print(move_zero_to_end1([0, 0,3,23,32] ))