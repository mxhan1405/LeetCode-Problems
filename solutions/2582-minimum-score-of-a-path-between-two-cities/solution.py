from collections import deque, defaultdict
import math

class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        # Step 1: Build the adjacency list graph
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # Step 2: BFS initialization
        queue = deque([1])
        visited = {1}
        min_score = math.inf
        
        # Step 3: Traverse the connected component
        while queue:
            node = queue.popleft()
            
            for neighbor, weight in graph[node]:
                # Update the minimum score with every edge encountered in this component
                min_score = min(min_score, weight)
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score

