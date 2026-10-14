class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = ["+", "-", "*", "/"]
        for token in tokens:
            if token in operator:
                int2 = stack.pop()
                int1 = stack.pop()
                if token == "+":
                    res = int1 + int2
                    stack.append(res)
                elif token == "-":
                    stack.append(int1 - int2)
                elif token == "*":
                    stack.append(int1 * int2)
                elif token == "/":
                    stack.append(int(int1 / int2))
            else:
                stack.append(int(token))
        return stack.pop()
