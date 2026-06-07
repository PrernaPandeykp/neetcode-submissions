class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            res[num] = res.get(num,0) + 1
        sortedDict = dict(sorted(res.items(), key = lambda item: item[1], reverse = True))

        return list(sortedDict.keys())[:k]
