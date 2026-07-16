import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefix_gcd = []
        current_max = float('-inf')
        
        # Step 1: Construct the prefix GCD array
        for num in nums:
            current_max = max(current_max, num)
            prefix_gcd.append(math.gcd(num, current_max))
            
        # Step 2: Sort the array in non-decreasing order
        prefix_gcd.sort()
        
        # Step 3: Pair the elements from both ends
        total_sum = 0
        left = 0
        right = len(prefix_gcd) - 1
        
        while left < right:
            total_sum += math.gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1
            
        return total_sum

