class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strings = ''

        for i in range(len(digits)):
            strings += str(digits[i])

        numbers = str(int(strings) + 1)

        res = [int(nums) for nums in numbers]

        return res