class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        high = len(nums) - 1
        low = 0

        while low <= high:
            potential_target = (high + low)//2
            if target == nums[potential_target]:
                return potential_target

            if nums[potential_target] >= target:
                high = potential_target - 1
            else:
                low = potential_target + 1 
        return -1
        