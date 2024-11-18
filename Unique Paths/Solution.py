class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1] * n

        for i in range(m -1):
            cur = [1] * n
            for j in range(1, n):
                cur[j] = cur[j - 1] + prev[j]
            prev = cur

        return prev[-1]