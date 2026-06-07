class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        maxProfit = 0
        for s in prices:
            maxProfit = max(maxProfit, s - min_buy)
            min_buy = min(min_buy, s)
        
        return maxProfit