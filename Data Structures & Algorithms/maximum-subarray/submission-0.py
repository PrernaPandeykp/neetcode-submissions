class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentMax = resMax = nums[0]

        for num in nums[1:]:
            currentMax = max(currentMax + num, num)
            resMax = max(currentMax, resMax)

        return resMax
