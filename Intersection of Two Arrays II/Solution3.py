class Solution3:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1.sort()
        nums2.sort()

        def searchFunc(nums1, nums2): 
            for n in nums1:
                l, r = 0, len(nums2) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if nums2[mid] < n:
                        l = mid + 1
                    elif nums2[mid] > n:
                        r = mid - 1
                    else:
                        res.append(nums2[mid])
                        nums2.pop(mid)
                        break

        if len(nums1) < len(nums2):
            searchFunc(nums1, nums2)
        else:
            searchFunc(nums2, nums1)

        return res