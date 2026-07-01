import collections
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
            
        # Step 1: Multi-source BFS to find the distance to the nearest thief for every cell
        q = collections.deque()
        dist = [[-1] * n for _ in range(n)]
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))
                    
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
                    
        # Step 2: Modified Dijkstra's using a max-heap
        # We store (-safeness, r, c) because Python's heapq is a min-heap
        pq = [(-dist[0][0], 0, 0)]
        # Use dist[0][0] as the min safeness seen so far for (0,0)
        max_safeness = [[-1] * n for _ in range(n)]
        max_safeness[0][0] = dist[0][0]
        
        while pq:
            safeness, r, c = heapq.heappop(pq)
            safeness = -safeness
            
            if r == n - 1 and c == n - 1:
                return safeness
                
            if safeness < max_safeness[r][c]:
                continue
                
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    # The safeness of the path to (nr, nc) is the minimum of current safeness and next cell's distance
                    new_safeness = min(safeness, dist[nr][nc])
                    if new_safeness > max_safeness[nr][nc]:
                        max_safeness[nr][nc] = new_safeness
                        heapq.heappush(pq, (-new_safeness, nr, nc))
                        
        return 0

