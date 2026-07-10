from typing import List
import bisect

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        unique_vals = sorted(list(set(nums)))
        m = len(unique_vals)
        
        comp_id = [0] * m
        curr_id = 0
        for i in range(1, m):
            if unique_vals[i] - unique_vals[i - 1] > maxDiff:
                curr_id += 1
            comp_id[i] = curr_id
            
        val_to_idx = {val: i for i, val in enumerate(unique_vals)}
        
        LOG_M = 18 
        jump = [[0] * LOG_M for _ in range(m)]
        
        for i in range(m):
            target_val = unique_vals[i] + maxDiff
            farthest_idx = bisect.bisect_right(unique_vals, target_val) - 1
            jump[i][0] = farthest_idx
            
        for j in range(1, LOG_M):
            for i in range(m):
                jump[i][j] = jump[jump[i][j-1]][j-1]
                
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            val_u, val_v = nums[u], nums[v]
            if val_u == val_v:
                ans.append(1)
                continue
                
            if val_u > val_v:
                val_u, val_v = val_v, val_u
                
            idx_u = val_to_idx[val_u]
            idx_v = val_to_idx[val_v]
            
            if comp_id[idx_u] != comp_id[idx_v]:
                ans.append(-1)
                continue
                
            steps = 0
            curr = idx_u
            
            for j in range(LOG_M - 1, -1, -1):
                if jump[curr][j] < idx_v:
                    curr = jump[curr][j]
                    steps += (1 << j)
                    
            ans.append(steps + 1)
            
        return ans

