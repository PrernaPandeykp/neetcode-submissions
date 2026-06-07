class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashNum = {}

        for i, num in enumerate(nums):
            hashNum[num] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashNum and hashNum[diff] != i:
                return [i, hashNum[diff]]

        return []