class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # hardcode:
        res = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product = product * nums[j]
            res.append(product)
        return res