class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        :type prices: List[int]
        :rtype: int
        """
        #If you want the max profit, you would want to find the lowest day to sell, and then highest day to sell 
        #Since this cannot be sorted, can go through the array and keep track of the lowest day and highest day. 
        #By default the first day is the "lowest" day. 
        buyDay = 0
        sellDay = 0
        largestProfit = 0

        for i,price in enumerate(prices): 
            if i == 0 or price < buyDay: 
                buyDay = price
            else:
                sellDay = price 
                #Only calculate the profit when a new sellday is found, or else the algorithm will calculate a profit of a day before the buy day

                largestProfit = max(largestProfit, sellDay - buyDay)
        return largestProfit
        