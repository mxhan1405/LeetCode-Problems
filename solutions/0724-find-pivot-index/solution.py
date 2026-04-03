class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i, x in enumerate(nums):
            # Right sum is total minus everything up to index i
            right_sum = total_sum - left_sum - x
            
            if left_sum == right_sum:
                return i
            
            # Update left_sum for the next index
            left_sum += x
            
        return -1

