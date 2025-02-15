class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows, num_cols = len(matrix), len(matrix[0])

        top, bot = 0, num_rows - 1

        while top <= bot:
            target_row = (top + bot) // 2
            if target < matrix[target_row][0]:
                bot = target_row - 1
            elif target > matrix[target_row][-1]:
                top = target_row + 1
            else:
                break

        if not (top <= bot):
            return False

        target_row = (top + bot) // 2

        l, r = 0, num_cols - 1
        while l <= r:
            mid = (l + r) // 2
            if target < matrix[target_row][mid]:
                r = mid - 1
            elif target > matrix[target_row][mid]:
                l = mid + 1
            else:
                return True

        return False