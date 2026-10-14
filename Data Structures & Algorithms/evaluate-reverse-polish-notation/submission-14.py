class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        store = []
        summation = int(tokens[0])
        for val in tokens:
            if val != "+" and val != "-" and val != "*" and val != "/":
                store.append(int(val))
            else:
                num2 = store.pop()
                num1 = store.pop()
                if val == "+":
                    summation = num1 + num2
                elif val == "-":
                    summation = num1 - num2
                elif val == "*":
                    summation = num1 * num2
                elif val == "/":
                    summation = int(num1 / num2)
                store.append(summation)
        return summation
