class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        freqToNum  = [[] for i in range(len(nums) +1)]

        for item in freq.keys():
            freqToNum[freq[item]].append(item)

        res = []
        for i in range(len(freqToNum)-1, -1, -1):
            for num in freqToNum[i]:
                res.append(num)

                if len(res) == k:
                    return res

        return res