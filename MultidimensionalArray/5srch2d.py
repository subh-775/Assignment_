# SEARCH 2D MATRIX

def searchMatrix(matrix: list[list[int]], target: int):
    total_rows = len(matrix)
    total_columns = len(matrix[0])
    row = 0
    column = total_columns-1
    while row < total_rows :
        num = matrix[row][column]
        if num == target:
            return True
        if num > target:
            mat = matrix[row]
            left = 0
            right = total_columns - 1
            
            if mat[left] == target:
                return True
            if mat[right] == target:
                return True
            
            while right >= left:
                mid = (right + left) // 2
                if mat[mid] > target:
                    right = mid - 1
                elif mat[mid] < target:
                    left = mid + 1
                else:
                    return True
            return False    
        row+=1
        
    return False
