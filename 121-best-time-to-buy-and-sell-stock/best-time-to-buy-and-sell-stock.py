class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice=float('inf')
        maxProfit=0
        for price in prices:
            if price < minPrice:
                minPrice=price
            profit=price-minPrice
            maxProfit=max(maxProfit,profit)
        return maxProfit

        