class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        
        # Option 1: The three largest numbers
        # Option 2: The two smallest (negative) numbers * the largest number
        return max(nums[-1] * nums[-2] * nums[-3], 
                   nums[0] * nums[1] * nums[-1])

