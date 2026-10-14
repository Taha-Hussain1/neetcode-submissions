class Solution:
    def isValid(self, s: str) -> bool:
        """"
        ok lets think about this
        input : []
        so base case if its "(, { or ["
        we need to add it to the stack
        now a stack is last in first out
        so if we put in [ last then we are expecting
        either ] or one of the three inputs
        otherwise return false
        """
        stack = []
        for bracket in s:
            if bracket == "(" or bracket == "{" or bracket == "[":
                stack.append(bracket)
            else: 
                if not stack:
                    return False
                last_bracket = stack.pop()
                if (last_bracket == "(" and bracket != ")" or
                last_bracket == "{" and bracket != "}" or
                last_bracket == "[" and bracket != "]"):
                    return False
        if stack:
            return False
        return True
             