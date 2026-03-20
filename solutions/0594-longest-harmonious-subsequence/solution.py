from collections import Counter

class Solution:
    def findLHS(self, nums: list[int]) -> int:
        # Count the frequency of each number
        counts = Counter(nums)
        max_length = 0
        
        # Iterate through the unique numbers in the counter
        for x in counts:
            # Check if a consecutive number x + 1 exists
            if x + 1 in counts:
                # The length is the sum of frequencies of x and x + 1
                max_length = max(max_length, counts[x] + counts[x + 1])
                
        return max_length

