class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        res = []

        for n in nums:
            if n in hm:
                hm[n] += 1
            else:
                hm[n] = 1

        sortedHm = dict(sorted(hm.items(), key=lambda item: item[1], reverse = True))

        for i, key in enumerate(sortedHm):
            if i >= k:
                break
            res.append(key)

        return res