class Solution2:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''

        w1, w2 = 0, 0

        while w1 < len(word1) and w2 < len(word2):
            merged += word1[w1]
            merged += word2[w2]
            w1 += 1
            w2 += 1
        merged += word1[w1:]
        merged += word2[w2:]

        return merged