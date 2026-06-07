class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in diff:
                return [diff[comp],i]

            diff[nums[i]] =i
        return []