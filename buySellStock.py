class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        max = 0
        min = prices[0]
        
        for price in prices:
            if price < min:
                min = price
            elif price - min > max:
                max = price - min

        return max