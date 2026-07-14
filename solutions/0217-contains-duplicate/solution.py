class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # This executes purely in C. No slow Python loop overhead.
        return len(nums) != len(set(nums))

