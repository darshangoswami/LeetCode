class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = defaultdict(int)

        for c in s:
            count[ord(c)] += 1

        for c in t:
            count[ord(c)] -= 1

        for val in count.values():
            if val != 0:
                return False

        return True