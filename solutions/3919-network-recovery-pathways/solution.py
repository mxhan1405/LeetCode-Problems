from heapq import heappush, heappop
from math import inf
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        
        # Build adjacency list, filtering out edges connected to offline nodes
        # Nodes 0 and n-1 are always online per problem description
        g = [[] for _ in range(n)]
        low, high = inf, -1
        
        for u, v, cost in edges:
            if not online[u] or not online[v]:
                continue
            g[u].append((v, cost))
            if cost < low:
                low = cost
            if cost > high:
                high = cost
                
        # If no edges exist at all, check if node 0 is already the target
        if low == inf:
            return 0 if n == 1 else -1

        # Helper function using Dijkstra to check if a valid path exists 
        # where every edge cost is >= mid, and total path cost <= k
        def check(mid: int) -> bool:
            dist = [inf] * n
            dist[0] = 0
            pq = [(0, 0)]  # (current_total_cost, node)
            
            while pq:
                d, u = heappop(pq)
                
                if d > k:
                    continue
                if u == n - 1:
                    return True
                if dist[u] < d:
                    continue
                    
                for v, cost in g[u]:
                    # Enforce the bottleneck threshold constraint
                    if cost < mid:
                        continue
                    if dist[u] + cost < dist[v]:
                        dist[v] = dist[u] + cost
                        if dist[v] <= k:
                            heappush(pq, (dist[v], v))
            return False

        # If the minimum possible edge constraint fails, no path exists at all
        if not check(low):
            return -1
            
        # Binary search for the maximum possible minimum edge cost
        ans = low
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid       # Valid path found, try a higher bottleneck
                low = mid + 1
            else:
                high = mid - 1  # Threshold too strict, lower it
                
        return ans

