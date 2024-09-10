# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter(root, res):
            if not root: return 0

            lHeight = diameter(root.left, res)
            rHeight = diameter(root.right, res)

            height = max(lHeight, rHeight) + 1

            res[0] = max(res[0], lHeight + rHeight)

            return height

        res = [0]

        diameter(root, res)

        return res[0]