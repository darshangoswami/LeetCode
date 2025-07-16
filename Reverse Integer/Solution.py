class Solution:
    def reverse(self, x: int) -> int:
        negative = False

        x_str = str(x)[::-1]
        if x_str[-1] == "-":
            x_str = x_str[:-1]
            negative = True

        num = (int(x_str) * -1) if negative else int(x_str)

        return num if (-2 ** 31) < num < ((2 ** 31) - 1) else 0