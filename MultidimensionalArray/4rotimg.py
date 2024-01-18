# ROTATE IMAGE
def rotate(matrix: list[list[int]]) -> None:
    row = 0
    column = 0
    total_rows = len(matrix)
    total_columns = len(matrix[0])
    while row < total_rows and column < total_columns:
        matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]
        if column == total_columns-1:
            row+=1
            column = row
        else:
            column+=1
    i = 0
    j = 0
    k = total_columns-1
    while i < total_rows:
        matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
        if j>=(total_columns-1)//2:
            j=0
            k=total_columns-1
            i+=1
        else:
            j+=1
            k-=1


matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotate(matrix)
print(matrix)

#[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]