class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            checkDup = set()
            for j in range(9):
                if board[i][j] != "." and board[i][j] in checkDup:
                    return False
                else:
                    checkDup.add(board[i][j])

        for i in range(9):
            checkDup = set()
            for j in range(9):
                if board[j][i] != "." and board[j][i] in checkDup:
                    return False
                else:
                    checkDup.add(board[j][i])

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                checkDup = set()
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        if board[r][c] != ".":
                            if board[r][c] in checkDup:
                                return False
                            checkDup.add(board[r][c])

        return True