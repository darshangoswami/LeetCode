class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        pos = 0

        for c in columnTitle[::-1]:
            mul = 26 ** pos
            res += (ord(c) - 64) * mul
            pos += 1
    
        return res