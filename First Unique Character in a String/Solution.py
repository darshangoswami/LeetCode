class Solution:
    def firstUniqChar(self, s: str) -> int:
        noRep = {}

        for c in s:
            if c in noRep:
                noRep[c] += 1
            else:
                noRep[c] = 1

        for char in noRep:
            if noRep[char] == 1:
                return s.index(char)
        
        return -1