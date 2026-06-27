from collections import Counter
import math

class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        counts = Counter(nums)
        max_length = 1  # Any single element forms a valid subset of length 1
        
        # Special Case: The number 1 (1 squared is always 1)
        if 1 in counts:
            ones_count = counts[1]
            # Must be an odd number of elements to maintain the peak pattern
            if ones_count % 2 == 0:
                max_length = max(max_length, ones_count - 1)
            else:
                max_length = max(max_length, ones_count)
        
        # Process all other numbers > 1
        for num in counts:
            if num == 1:
                continue
                
            current_length = 0
            current_num = num
            
            # Follow the chain x -> x^2 -> x^4 -> x^8...
            while current_num in counts and counts[current_num] >= 2:
                current_length += 2
                current_num = current_num * current_num
                
            # If the final element in the chain exists at least once, it can be the peak
            if current_num in counts:
                current_length += 1
            else:
                # If it doesn't exist, the last element we counted 2 of must act as the peak
                current_length -= 1
                
            max_length = max(max_length, current_length)
            
        return max_length

