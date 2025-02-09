class Solution2:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : lambda a,b: int(a / b)
        }

        for n in tokens:
            if n.lstrip('-').isdigit():
                stack.append(int(n))
            elif n in ops:
                if len(stack) >= 2:
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(ops[n](a, b))

        return stack.pop() if stack else 0