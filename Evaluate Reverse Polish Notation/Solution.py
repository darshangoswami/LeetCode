class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for n in tokens:
            if n.lstrip('-').isnumeric():
                stack.append(int(n))
            else:
                b = stack.pop()
                a = stack.pop()
                if n == "+":
                    tempRes = a + b
                elif n == "-":
                    tempRes = a - b
                elif n == "*":
                    tempRes = a * b
                elif n == '/':
                    tempRes = int(a / b)
                stack.append(tempRes)

        return stack[-1]