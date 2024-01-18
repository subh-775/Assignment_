# SPIRAL ORDER MATRIX

def spiralOrder(matrix: list[list[int]]) -> list[int]:
    if not matrix or not matrix[0]:
        return []

    rows, cols = len(matrix), len(matrix[0])
    result = []
    left, right, top, bottom = 0, cols - 1, 0, rows - 1

    while left <= right and top <= bottom:

        for i in range(left, right + 1):
            result.append(matrix[top][i])

        for i in range(top + 1, bottom + 1):
            result.append(matrix[i][right])

        if top < bottom and left < right:

            for i in range(right - 1, left, -1):
                result.append(matrix[bottom][i])

            for i in range(bottom, top, -1):
                result.append(matrix[i][left])

        left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

    return result

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))

