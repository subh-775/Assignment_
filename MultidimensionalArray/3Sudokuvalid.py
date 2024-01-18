def isValidSudoku(board: list[list[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    temp = board[i][j]

                    # Row Check
                    for k in range(9):
                        if k == j:
                            continue
                        if board[i][k] == temp:
                            return False

                    # Column Check
                    for k in range(9):
                        if k == i:
                            continue
                        if board[k][j] == temp:
                            return False

                    # Matrix Check
                    xbox = i - i % 3
                    ybox = j - j % 3
                    for k in range(xbox, xbox + 3):
                        for l in range(ybox, ybox + 3):
                            if k == i and l == j:
                                continue
                            if board[k][l] == temp:
                                return False

        return True