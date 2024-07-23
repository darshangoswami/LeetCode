class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(1, numRows):
            temp = [0] + res[-1] + [0]
            cur = []
            for j in range(len(res[-1]) + 1):
                cur.append(temp[j] + temp[j + 1])
            res.append(cur)

        return res