# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        self.k = k

        def dfs(node):
            if not node or k == 0:
                return

            dfs(node.left)

            self.k -= 1
            res.append(node.val)

            dfs(node.right)

        dfs(root)

        return res[k - 1]