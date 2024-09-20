class Solution:
    def myAtoi(self, s: str) -> int:
        res = ''
        s = s.strip()
        sign = 1

        if not s:
            return 0

        if s[0] == '-' or s[0] == '+':
            sign = -1 if s[0] == '-' else 1
            s = s[1:] 

        for c in s:
            if c.isdigit():
                res += c
            else:
                break

        if not res:
            return 0

        res = int(res) * sign

        INT_MAX = (2 ** 31) - 1
        INT_MIN = -2 ** 31
        if res > INT_MAX:
            return INT_MAX
        elif res < INT_MIN:
            return INT_MIN

        return res