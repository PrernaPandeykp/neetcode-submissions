class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        
        l = len(nums)
        prefix = postfix = 1
        for i in range(l):
            output.append(prefix)
            prefix *=nums[i]

        for i in range(l-1, -1, -1):
            output[i] *= postfix
            postfix *=nums[i]

        return output
        

        

