class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, trash in enumerate(nums):
            for j, trash2 in enumerate(nums):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]
        return None