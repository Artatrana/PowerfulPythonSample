# You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees (clockwise).
# You have to rotate the image in place, meaning you have to modify the input matrix directly.
def rotate_image(matrix: list) -> list:
    n = len(matrix[0])
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()
    return matrix

print (rotate_image([
 [1,2,3],
 [4,5,6],
 [7,8,9]
]))

def rotate_180(matrix: list) -> list:
    n = len(matrix)
    for i in range(n//2):
        matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]

    for i  in range(n):
        matrix[i].reverse()
    return matrix

print (rotate_180([
 [1,2,3],
 [4,5,6],
 [7,8,9]
]))

def rotate_counter_clockwise(matrix):
    n = len(matrix)
    # Step 1: Transpose
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # step 2: reverse each column
    for i in range(n):
        for j in range(n//2):
            matrix[i][n-1-i], matrix[n-1-i][i]=  matrix[n-1-i][i],  matrix[i][n-1-i]
    return matrix


print (rotate_counter_clockwise([
 [1,2,3],
 [4,5,6],
 [7,8,9]
]))

def rotate(matrix):
    n = len(matrix)

    # this is going to transpose the matrix
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()

    return matrix

print (rotate([
 [1,2,3],
 [4,5,6],
 [7,8,9]
]))
