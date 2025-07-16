class Solution2:
    def reverse(self, x: int) -> int:
        negative = -1 if x < 0 else 1
        x = abs(x)
        res = 0

        while x:
            pop = x % 10
            x = x // 10
            res = res * 10 + pop

        res = res * negative

        return res if (-2 ** 31) < res < ((2 ** 31) - 1) else 0