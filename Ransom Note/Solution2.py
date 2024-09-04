class Solution2:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran = Counter(ransomNote)
        mag = Counter(magazine)

        if ran & mag == ran:
            return True
        return False