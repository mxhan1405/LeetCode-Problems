class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        total_elements = m * n
        
        # Optimize k if it is larger than the total number of elements
        k = k % total_elements
        
        # Initialize an empty result grid with the same dimensions
        ans = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                # 1. Convert 2D index (i, j) to a flattened 1D index
                # 2. Add the shift 'k' and apply modulo arithmetic for wrapping
                new_1d_index = (i * n + j + k) % total_elements
                
                # 3. Convert the new 1D index back to 2D coordinates (row, col)
                new_row = new_1d_index // n
                new_col = new_1d_index % n
                
                # Place the element into its shifted position
                ans[new_row][new_col] = grid[i][j]
                
        return ans

