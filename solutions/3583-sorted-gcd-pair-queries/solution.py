from bisect import bisect_right
from itertools import accumulate

class Solution:
    def gcdValues(self, nums: list[int], queries: list[int]) -> list[int]:
        max_num = max(nums)
        
        # 1. Count the frequency of each number in nums
        freq = [0] * (max_num + 1)
        for num in nums:
            freq[num] += 1
            
        # 2. Count how many elements in nums are multiples of each number `i`
        count_multiples = [0] * (max_num + 1)
        for i in range(1, max_num + 1):
            for j in range(i, max_num + 1, i):
                count_multiples[i] += freq[j]
                
        # 3. Calculate exact number of pairs with GCD equal to `i`
        # Using a sieve approach from large to small
        gcd_pair_counts = [0] * (max_num + 1)
        for i in range(max_num, 0, -1):
            # Total combinations of pairs whose elements share a common divisor `i`
            c = count_multiples[i]
            total_pairs = c * (c - 1) // 2
            
            # Subtract pairs that have a strictly larger common divisor (multiples of i)
            for j in range(2 * i, max_num + 1, i):
                total_pairs -= gcd_pair_counts[j]
                
            gcd_pair_counts[i] = total_pairs
            
        # 4. Create a prefix sum array to map indices to actual GCD values
        prefix_sums = list(accumulate(gcd_pair_counts))
        
        # 5. Answer each query using binary search
        ans = []
        for q in queries:
            # Find the first GCD value whose prefix sum strictly exceeds `q`
            idx = bisect_right(prefix_sums, q)
            ans.append(idx)
            
        return ans

