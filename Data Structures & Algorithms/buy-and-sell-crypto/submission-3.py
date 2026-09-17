class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestPrice = prices[0]
        maxProfit = 0

        for i in prices:
            if i < lowestPrice:
                lowestPrice = i

            profit = i - lowestPrice
            if profit > maxProfit:
                maxProfit = profit

        return maxProfit
            
