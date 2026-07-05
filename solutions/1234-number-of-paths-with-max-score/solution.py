
class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        MOD = 10**9 + 7
        n = len(board)
        
        # dp[i][j] stores [max_score, path_count]
        # Initialize with [-1, 0] to represent unreached/invalid states
        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]
        
        # Base case: Starting point 'S' at bottom-right
        dp[n-1][n-1] = [0, 1]
        
        # Traverse the grid backwards from bottom-right to top-left
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] in ('S', 'X'):
                    continue  # 'S' is already handled; 'X' is blocked
                
                max_score = -1
                path_count = 0
                
                # Check the 3 possible cells we could have come from
                # (Right, Down, Bottom-Right)
                for di, dj in [(0, 1), (1, 0), (1, 1)]:
                    ni, nj = i + di, j + dj
                    
                    if ni < n and nj < n and dp[ni][nj][0] != -1:
                        prev_score, prev_count = dp[ni][nj]
                        
                        if prev_score > max_score:
                            max_score = prev_score
                            path_count = prev_count
                        elif prev_score == max_score:
                            path_count = (path_count + prev_count) % MOD
                
                # If at least one valid path reached this cell, add current cell's value
                if max_score != -1:
                    current_val = 0 if board[i][j] == 'E' else int(board[i][j])
                    dp[i][j] = [max_score + current_val, path_count]
        
        # Top-left cell 'E' holds our final answer
        final_score, final_count = dp[0][0]
        return [max(0, final_score), final_count]

