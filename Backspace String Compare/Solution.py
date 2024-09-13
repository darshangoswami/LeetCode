class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def finalString(string):
            stack = []

            for c in string:
                if c != '#':
                    stack.append(c)
                elif stack:
                    stack.pop()
            
            return ''.join(stack)

        s1 = finalString(s)
        t1 = finalString(t)

        return s1 == t1