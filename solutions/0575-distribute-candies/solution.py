class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        # Alice can eat at most n / 2 candies
        limit = len(candyType) // 2
        # Count how many unique types of candies there are
        unique_types = len(set(candyType))
        
        # The answer is the smaller of the two values
        return min(unique_types, limit)

