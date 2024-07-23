# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return (self.DFS(root) >= 0)
    
    def DFS(self, root):
        if not root: return 0

        lHeight, rHeight = self.DFS(root.left), self.DFS(root.right)

        if lHeight < 0 or rHeight < 0 or abs(lHeight - rHeight) > 1: return -1

        return max(lHeight, rHeight) + 1
