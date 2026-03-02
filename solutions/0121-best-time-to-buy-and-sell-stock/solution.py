class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the minimum price to a very high value
        # and the maximum profit to 0
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update min_price if the current price is lower
            if price < min_price:
                min_price = price
            # Calculate profit if we sold at the current price
            # and update max_profit if it's the highest seen so far
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit

