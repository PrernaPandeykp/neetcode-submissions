class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1]*(len(nums)+1)
        ans = 0
        for i in range(len(nums)):
            for j in range(0,i):
                if nums[j]<nums[i]:
                    lis[i] = max(lis[i], lis[j] +1)

        return max(lis)
