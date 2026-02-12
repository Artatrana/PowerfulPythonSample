def sort_list(num : list[int]) -> list[int]:
    for i in range(len(num)):
        for j in range(i, len(num)):
            if num[i] > num[j]:
                num[i] , num[j] = num[j], num[i]

    return num 

print(sort_list([20,4,5,59,90,34,45]))

