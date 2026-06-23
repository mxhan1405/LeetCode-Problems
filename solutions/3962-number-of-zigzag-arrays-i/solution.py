class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        num_values = r - l + 1
        
        # Base case for array of length 1 (if n can be 1, return the total possible numbers)
        if n == 1:
            return num_values
            
        # dp_up[v]: valid paths ending at index 'v' via an increasing step
        # dp_down[v]: valid paths ending at index 'v' via a decreasing step
        # Value 'v' maps to index 'v - l'
        dp_up = [0] * num_values
        dp_down = [0] * num_values
        
        # Initializing for length 2
        for i in range(num_values):
            dp_up[i] = i                     # Elements smaller than i
            dp_down[i] = num_values - 1 - i  # Elements larger than i

        # Transition for lengths 3 to n
        for _ in range(3, n + 1):
            next_up = [0] * num_values
            next_down = [0] * num_values
            
            # Prefix sums of dp_down for 'up' transitions
            pref_down = 0
            for i in range(num_values):
                next_up[i] = pref_down % MOD
                pref_down += dp_down[i]
                
            # Suffix sums of dp_up for 'down' transitions
            suff_up = 0
            for i in range(num_values - 1, -1, -1):
                next_down[i] = suff_up % MOD
                suff_up += dp_up[i]
                
            dp_up = next_up
            dp_down = next_down
            
        return (sum(dp_up) + sum(dp_down)) % MOD

