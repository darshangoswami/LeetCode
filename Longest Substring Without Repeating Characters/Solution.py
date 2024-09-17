class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()

        res = 0
        left = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            res = max(res, right - left + 1)

        return res