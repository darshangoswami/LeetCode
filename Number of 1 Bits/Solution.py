class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        bInt = str(bin(n)[2:])

        for b in bInt:
            if b == "1":
                count += 1

        return count