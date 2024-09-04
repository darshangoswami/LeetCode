class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_mag = {}

        for c in magazine:
            if c in count_mag:
                count_mag[c] += 1
            else:
                count_mag[c] = 1

        for c in ransomNote:
            if count_mag.get(c, 0):
                count_mag[c] -= 1
            else:
                return False

        return True