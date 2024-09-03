class Solution2:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        def searchFunc(nums1, nums2):
            for n in nums1:
                if n in nums2:
                    res.append(n)
                    nums2.remove(n)

        if len(nums1) < len(nums2):
            searchFunc(nums1, nums2)
        else:
            searchFunc(nums2, nums1)

        return res