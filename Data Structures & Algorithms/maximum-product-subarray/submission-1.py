class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProduct = maxProduct = 1
        res = nums[0]
    
        for num in nums:
            temp = num*maxProduct
            maxProduct = max(maxProduct*num, minProduct*num, num)
            minProduct = min(temp , minProduct*num, num)

            res = max(res, maxProduct)

        return res