class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i, j, wordPosition):
            if wordPosition == len(word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n:
                return

            if board[i][j] != word[wordPosition]:
                return

            temp = board[i][j]
            board[i][j] = 0

            found = (dfs(i, j + 1, wordPosition + 1) or
                     dfs(i, j - 1, wordPosition + 1) or
                     dfs(i + 1, j, wordPosition + 1) or
                     dfs(i - 1, j, wordPosition + 1))

            board[i][j] = temp
            return found

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True