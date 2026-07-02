from collections import deque

class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        # min_cost[r][c] stores the minimum health lost to reach cell (r, c)
        min_cost = [[float('inf')] * n for _ in range(m)]
        
        # Initialize starting cell
        min_cost[0][0] = grid[0][0]
        
        # Deque for 0-1 BFS: stores tuples of (row, col)
        queue = deque([(0, 0)])
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            r, c = queue.popleft()
            
            # If we reached the bottom-right corner, check if health remains positive
            if r == m - 1 and c == n - 1:
                return min_cost[r][c] < health
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check boundaries
                if 0 <= nr < m and 0 <= nc < n:
                    new_cost = min_cost[r][c] + grid[nr][nc]
                    
                    # If we found a path with a strictly lower health loss
                    if new_cost < min_cost[nr][nc]:
                        min_cost[nr][nc] = new_cost
                        
                        # 0-1 BFS optimization
                        if grid[nr][nc] == 0:
                            queue.appendleft((nr, nc)) # Cost 0 -> Front
                        else:
                            queue.append((nr, nc))     # Cost 1 -> Back
                            
        return min_cost[m - 1][n - 1] < health

