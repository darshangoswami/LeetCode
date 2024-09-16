class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''

        w1, w2 = len(word1), len(word2)
        i = 0

        while w1 or w2:
            if w1 != 0:
                merged += word1[i]
                w1 -= 1
            if w2 != 0:
                merged += word2[i]
                w2 -=1
            i += 1
            
        return merged