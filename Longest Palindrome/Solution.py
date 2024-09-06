class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        res = 0
        odd = 0

        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1

        for c in count:
            if count[c] % 2 == 0:
                res += count[c]
            else:
                res += count[c] - 1
                odd = 1
        
        return res + odd