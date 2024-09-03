class Solution4:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        checkMap = {}

        for n in nums1:
            if n in checkMap:
                checkMap[n] += 1
            else:
                checkMap[n] = 1
        
        for n in nums2:
            if n in checkMap and checkMap[n] > 0:
                res.append(n)
                checkMap[n] -= 1

        return res