class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        heap = []

        for num in nums:
            count[num] += 1
        
        for key, value in count.items():
            heapq.heappush(heap, (-value, key))
        
        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        return res
        # create a dict that will count all the frequencies of the elements
        # put the frequencies into a maxheap and return the key
        # I think i can convert the list of frequencies into a maxheap using heapify
        # After that i somehow need to keep the key...
        # OK I REMEMBER
        # Insert a tuple (frequency, key)   
        # ez

        


