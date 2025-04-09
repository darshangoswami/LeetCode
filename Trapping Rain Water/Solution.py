class Solution:
    def trap(self, height: List[int]) -> int:
        left_wall = right_wall = 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n

        for i in range(n):
            j = -i - 1
            max_left[i] = left_wall
            max_right[j] = right_wall

            left_wall = max(left_wall, height[i])
            right_wall = max(right_wall, height[j])

        res = 0
        for i in range(n):
            cur = min(max_left[i], max_right[i])
            res += max(0, cur - height[i])

        return res