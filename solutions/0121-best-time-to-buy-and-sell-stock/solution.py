class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Start with an insanely high price
        max_profit = 0            # Start with zero profit
        
        for price in prices:
            # 1. Track the lowest price we have seen so far
            if price < min_price:
                min_price = price
            # 2. Check if selling today beats our best recorded profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit

