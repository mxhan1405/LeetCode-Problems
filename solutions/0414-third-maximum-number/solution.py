class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        # Get distinct numbers only
        unique_nums = sorted(list(set(nums)), reverse=True)
        
        # If 3 or more exist, return the third one; otherwise, return the first (max)
        return unique_nums[2] if len(unique_nums) >= 3 else unique_nums[0]

