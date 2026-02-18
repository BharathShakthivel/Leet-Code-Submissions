class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0
        for r in range(1,len(prices)):
            if prices[r]<prices[l]:
                l = r
            cur_profit = prices[r]-prices[l]
            max_profit = max(max_profit,cur_profit)
        return max_profit
