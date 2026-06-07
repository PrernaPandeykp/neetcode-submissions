class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        
        heap = []
        for item in freq.keys():
            heapq.heappush(heap, (freq[item], item))

            if len(heap) > k:
                heapq.heappop(heap)

        return [num for count, num in heap]

        
