class Solution2:
    def gcdCal(self, a, b):
            while b:
                a, b = b, a % b
            return abs(a)


    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''

        return str1[:self.gcdCal(len(str1), len(str2))]