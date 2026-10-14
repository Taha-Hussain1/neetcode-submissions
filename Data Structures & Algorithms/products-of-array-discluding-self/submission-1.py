class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums) + 1)
        postfix = [1] * (len(nums) + 1)
        prefix_prod = 1
        postfix_prod = 1
        for i in range(len(nums)):
            prefix[i + 1] = nums[i] * prefix_prod
            postfix[len(nums) -1 - i] = nums[len(nums) - 1 - i] * postfix_prod
            prefix_prod = prefix_prod * nums[i]
            postfix_prod = postfix_prod * nums[len(nums) - 1 - i]
        output = []
        for i in range(0, len(nums)):
            output.append(prefix[i] * postfix[i + 1])
        return output
