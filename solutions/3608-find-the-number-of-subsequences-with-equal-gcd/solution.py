import math
from functools import lru_cache

class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        @lru_cache(None)
        def dp(idx, gcd1, gcd2):
            # Base case: when all elements are processed
            if idx == n:
                # Both sequences must be non-empty and have equal GCD
                return 1 if gcd1 == gcd2 and gcd1 > 0 else 0
            
            num = nums[idx]
            
            # Choice 1: Skip the current number
            res = dp(idx + 1, gcd1, gcd2)
            
            # Choice 2: Add to the first subsequence
            res += dp(idx + 1, math.gcd(gcd1, num), gcd2)
            
            # Choice 3: Add to the second subsequence
            res += dp(idx + 1, gcd1, math.gcd(gcd2, num))
            
            return res % MOD
            
        # Start at index 0 with empty subsequences (represented by GCD = 0)
        return dp(0, 0, 0)

