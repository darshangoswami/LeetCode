class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        paraMap = {')' : '(', '}' : '{', ']' : '['}

        for c in s:
            if c in paraMap:
                if stack and stack[-1] == paraMap[c]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)

        return True if not stack else False
            