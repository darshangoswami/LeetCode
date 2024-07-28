class Solution:
    def isPalindrome(self, s: str) -> bool:
        og = rev = ''

        for c in s:
            if c.isalnum():
                og += c.lower()
                rev += c.lower()
        
        return og == rev[::-1]