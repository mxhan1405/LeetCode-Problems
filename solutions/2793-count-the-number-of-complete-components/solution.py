from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        vis = [0] * n

        def dfs(u):
            vis[u] = 1
            comp.append(u)
            for v in g[u]:
                if not vis[v]:
                    dfs(v)

        ans = 0
        for i in range(n):
            if not vis[i]:
                comp = []
                dfs(i)
                k = len(comp)
                if all(len(g[x]) == k - 1 for x in comp):
                    ans += 1

        return ans

