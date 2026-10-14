class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        heap = []
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for key, value in count.items():
            heapq.heappush(heap, (-value, key))
        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        return res

        


