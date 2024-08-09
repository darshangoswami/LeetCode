class Solution:
    def reverseBits(self, n: int) -> int:
        bits = bin(n)[2:].zfill(32)

        reversedBits = bits[::-1]

        return int(reversedBits, 2)