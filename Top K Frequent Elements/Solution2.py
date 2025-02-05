class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        freq = [[] for _ in range(len(nums) + 1)]
        res = []

        for n in nums:
            hm[n] = 1 + hm.get(n, 0)

        for n, c in hm.items():
            freq[c].append(n)

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res