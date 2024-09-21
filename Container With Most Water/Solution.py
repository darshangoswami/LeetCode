class Solution:
    def maxArea(self, height: List[int]) -> int:
        areaMax = 0
        p1, p2 = 0, len(height) - 1

        while p1 < p2:
            area = min(height[p1], height[p2]) * (p2 - p1)
            if area > areaMax:
                areaMax = area
            if height[p1] <= height[p2]:
                p1 += 1
            else:
                p2 -= 1

        return areaMax