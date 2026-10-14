class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        sortedNum = sorted(nums)
        prev = 1.5
        for i in range(len(nums)):
            if sortedNum[i] == prev:
                continue
            prev = sortedNum[i]
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if (sortedNum[j] + sortedNum[k] + sortedNum[i] == 0):
                        tmp = sortedNum[i], sortedNum[j], sortedNum[k]
                        triplets.add(tuple(tmp))

        return [list(i) for i in triplets]

