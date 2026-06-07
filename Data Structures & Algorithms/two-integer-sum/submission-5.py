class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashNum = {}

        for i, num in enumerate(nums):
            diff = target - nums[i]
            if diff in hashNum:
                return [hashNum[diff], i]

            hashNum[num] = i


        return []