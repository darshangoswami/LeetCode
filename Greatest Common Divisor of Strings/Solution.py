class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        gcdLength = math.gcd(len1, len2)
        res = ""

        for i in range(gcdLength):
            if str1[i] == str2[i]:
                res += str1[i]

        if str1 == res * (len1 // gcdLength) and str2 == res * (len2 // gcdLength):
            return res
        else:
            return ""