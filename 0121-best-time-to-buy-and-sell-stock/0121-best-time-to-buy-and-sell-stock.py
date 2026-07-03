class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_value = float("inf")
        
        for num in prices:
            if num < min_value:
                min_value = num
            else:
                profit = num - min_value
                if profit > max_profit:
                    max_profit = profit
        return max_profit

