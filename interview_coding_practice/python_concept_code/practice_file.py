# This code practice are form the below Github repository
# https://github.com/Tanu-N-Prabhu/Python/blob/master/Python%20Coding%20Interview%20Prep/Python%20Coding%20Interview%20Questions%20(Beginner%20to%20Advanced).md#-prepare-for-the-worst-most-frequently-asked-questions-by-big-tech-companies


import inspect
import re
# convert list into sting
def conver_list_str(lst):
    # str = ''.join(x for x in lst)
    str1 = ''.join(lst)
    print(str1)


def transpose_matrix(matrix):
    length= len(matrix)
    for i in range(length):
        for j in range(i+1, length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

def transpose_matrix1(matrix):
    return [list(row) for row in zip(*matrix)]

def compare_string(str1, str2):
    str1 = list(chr.upper() for chr in list(str1))
    str2 = list(chr.upper() for chr in list(str2))

    str1.sort()
    str2.sort()
    print(str1, str2)
    if str1 == str2:
        return "True"
    else:
        return "False"

# Counting Digits, Letters, and Spaces in a String
def counting_digits(str):
    digitCount = re.sub("[^0-9]","",str)
    letterCount = re.sub("[^a-zA-Z]","",str)
    spaceCount = re.findall("[ \n]", str)

    print(len(digitCount))
    print(len(letterCount))
    print(len(spaceCount))

# Building a Pyramid in Python
def building_pyramid(floor):
    h = 2*floor - 1
    for i in range(1, 2*floor, 2):
        print('{:^{}}'.format('*'*i,h))


if __name__ == "__main__":
    building_pyramid(3)

    # lst = ["P", "Y", "T", "H", "O", "N"]
    # conver_list_str(lst)

    # #matrix1 = [[1, 2, 3],[4, 5, 6],[ 7, 8,9]]
    # matrix2 = [[1, 2, 3], [4, 5, 6]]
    # print(transpose_matrix(matrix2))
    # print(transpose_matrix1(matrix2))
    #
    # transpose = transpose_matrix1(matrix2)
    # transpose.reverse()
    # print(transpose)

    # str1 = "Listen"
    # str2 = "Silent"
    #
    # print(compare_string(str1,str2))
    # name = 'Python is 1'
    # counting_digits(name)




