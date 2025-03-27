# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            rightVal = None

            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightVal = node
                    q.append(node.left)
                    q.append(node.right)
            if rightVal:        
                res.append(rightVal.val)

        return res