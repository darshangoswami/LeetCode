class Solution2:
    def backspaceCompare(self, s: str, t: str) -> bool:
        finalS = ""
        finalT = ""

        for c in s:
            if c != "#":
                finalS += c
            else:
                finalS = finalS[:-1]

        for c in t:
            if c != "#":
                finalT += c
            else:
                finalT = finalT[:-1]

        return finalS == finalT