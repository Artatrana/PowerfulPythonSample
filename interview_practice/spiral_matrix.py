def spiralOrder(matrix: list[list[int]]) -> list:
    if not matrix:
        return []

    row_begin = 0
    row_end = len(matrix)
    column_begin = 0
    column_end = len(matrix[0])

    result = []

    while row_begin < row_end and column_begin < column_end:
        # 1. Traverse from Left to Right
        for i in range(column_begin, column_end):
            result.append(matrix[row_begin][i])
        row_begin += 1

        # 2. Traverse downwards
        for j in range(row_begin, rowend):
            result.append(matrix[j][column_end - 1])
        column_end -= 1

        # 3. Traverse from Right to Left
        if row_begin < rowend:
            for i in range(column_end - 1, column_begin - 1, -1):
                result.append(matrix[row_begin - 1][i])
            rowend -= 1

        # 4. Traverse upwards
        if column_begin < column_end:
            for j in range(row_begin - 1, row_begin - 1, -1):
                result.append(matrix[j][column_begin])
            column_begin += 1

    return result
