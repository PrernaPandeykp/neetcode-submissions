class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        sorted_freq = dict(sorted(freq.items(), key=lambda x: x[1]))

        l = []
        c = 0
        for i in reversed(sorted_freq):
            if c==k:
                break
            l.append(i)
            c+=1

        return l
