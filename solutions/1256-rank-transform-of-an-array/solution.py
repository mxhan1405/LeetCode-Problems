class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        # 1. Deduplicate and sort the array to get unique values in ascending order
        unique_sorted = sorted(set(arr))
        
        # 2. Build a hash map where keys are numbers and values are their 1-based ranks
        rank_map = {num: rank for rank, num in enumerate(unique_sorted, 1)}
        
        # 3. Replace each original element with its corresponding rank
        return [rank_map[num] for num in arr]

