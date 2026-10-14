class Solution:
    def isValid(self, s: str) -> bool:
        # just count the number of each entry eh?
        # nah mate you have to make sure the closing brackets are in the correct order.
        # add the seen brackets to a array or stack?
        # remove from the data structure once their corresponding close bracket is seen


        num_open_1 = 0
        num_open_2 = 0
        num_open_3 = 0
        num_close_1 = 0
        num_close_2 = 0
        num_close_3 = 0
        seen = []
        if s[0] == ')' or s[0] == '}' or s[0] == ']':
            return False

        for val in s:
            if val == '(' or val == '{' or val == '[':
                seen.append(val)
            else:
                if not seen:
                    return False
                last_open = seen.pop()
                if (last_open == '(' and val != ')') or (last_open == '{' and val != '}') or (last_open == '[' and val != ']'):
                    return False


            if val == '(':
                num_open_1 += 1
            elif val == '{':
                num_open_2 += 1
            elif val == '[':
                num_open_3 += 1
            elif val == ')':
                num_close_1 += 1
            elif val =='}':
                num_close_2 += 1
            elif val == ']':
                num_close_3 += 1
        if num_open_1 == num_close_1 and num_open_2 == num_close_2 and num_open_3 == num_close_3:
            return True
        return False  