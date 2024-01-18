# FIND Kth SAMLLEST ELEMENT

def kthSmallest(matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        row = 0
        column = 0
        lst = []
        while row <= n-1 and column <= n-1:
            lst.append(matrix[row][column])
            if column == n-1:
                row+=1
                column=0
            else:
                column += 1
        return sorted(lst)[k-1]
