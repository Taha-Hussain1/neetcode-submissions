class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # note: target = num1 + num2
        # rearrange to: target - num1 = num2
        # requires space... 
        # note: array is in ascending order: use modified binary search 

        high = len(numbers) - 1
        low = 0
        while (high > low):
            if numbers[low] + numbers[high] == target:
                return [low + 1, high + 1]
            elif numbers[low] + numbers[high] > target:
                high -= 1
            elif numbers[low] + numbers[high] < target:
                low += 1 
    
    # hard-coded
    # def twoSum(self, numbers: List[int], target: int) -> List[int]: 
    #     for i in range(len(numbers)):
    #         for j in range(len(numbers)):
    #             if i != j and numbers[i] + numbers[j] == target:
    #                 return [i+1, j+1] 
    

        