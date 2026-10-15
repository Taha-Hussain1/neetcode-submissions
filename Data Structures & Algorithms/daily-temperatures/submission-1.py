class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
       
        """
        Ok for the legit solution we employ a stack.
        We compare the top of the stack with the new value and check 
        if its greater or not. Then if it is we pop the top value and
        then check the next top value

        We need to track the indexes of each value to calculate the 
        number we put in the output array as well as its position
        in the output array. Maybe insert a tuple?

        Finally at the end we need to put 0's in the remaining 
        slots i think that can be done easily by initalising
        a 0'd array
        """
        length = len(temperatures)
        output = [0] * length
        mr_stack = []
        for i in range(length):
            while mr_stack and temperatures[i] > mr_stack[-1][1]:
                index, val = mr_stack.pop()
                output[index] = i - index
            mr_stack.append((i, temperatures[i]))
            
        return output



       
       
       
       
        # [30, 38, 30, 36, 35, 40, 28]
        # [1, 4, 1, 2, 1, 0, 0]
        # brute force = double for loop ez
        output = []
        length = len(temperatures)
        for i in range(length):
            ticker = 1
            for j in range(length):
                if i >= j: 
                    continue
                if temperatures[i] < temperatures[j]:
                    output.append(ticker)
                    break
                elif j+1 == length:
                    output.append(0)
                ticker += 1
        output.append(0)
        return output

