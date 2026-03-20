class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        # Optimization: If n is 0, we're already done
        if n == 0: return True
        
        for i in range(len(flowerbed)):
            # Check if current plot is empty
            if flowerbed[i] == 0:
                # Check if left and right neighbors are empty or out of bounds
                prev_empty = (i == 0 or flowerbed[i - 1] == 0)
                next_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
                
                if prev_empty and next_empty:
                    # Plant a flower here
                    flowerbed[i] = 1
                    n -= 1
                    
                    # If we've planted all n flowers, return True early
                    if n == 0:
                        return True
                        
        return n <= 0

