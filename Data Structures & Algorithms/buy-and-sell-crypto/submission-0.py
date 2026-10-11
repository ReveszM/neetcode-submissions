class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxSpread = 0
        prevMin = 101

        for price in prices:
            maxSpread = max(maxSpread, price - prevMin)
            prevMin = min(prevMin, price)

        return maxSpread
        