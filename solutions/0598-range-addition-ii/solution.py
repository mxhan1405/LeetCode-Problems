class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        # If there are no operations, all m * n cells have the same max value (0)
        if not ops:
            return m * n
        
        # The maximum values will be in the intersection of all operation rectangles
        min_row = m
        min_col = n
        
        for r, c in ops:
            min_row = min(min_row, r)
            min_col = min(min_col, c)
            
        return min_row * min_col


