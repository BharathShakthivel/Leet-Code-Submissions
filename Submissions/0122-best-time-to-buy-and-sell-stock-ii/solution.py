class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(N) Time and Space Complexity
        profit = 0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit+= prices[i]-prices[i-1]
        return profit
