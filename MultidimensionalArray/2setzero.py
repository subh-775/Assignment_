# SET ZEROES
def setZeroes(matrix: list[list[int]]) -> None:
    total_rows = len(matrix)
    total_columns = len(matrix[0])
    row = 0
    column = 0
    zero_lst = []
    while row < total_rows and column < total_columns:
        chk_num = matrix[row][column]
        if chk_num==0:
            zero_lst.append([row,column])

        if column == total_columns-1:
            column = 0
            row+=1
        else:
            column+=1

    for zrow, zcol in zero_lst:    
        for i in range(0, total_columns):
            matrix[zrow][i] = 0
        for i in range(0, total_rows):
            matrix[i][zcol] = 0
