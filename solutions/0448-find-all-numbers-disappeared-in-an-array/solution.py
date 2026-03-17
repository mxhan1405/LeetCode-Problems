class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # Step 1: Mark numbers as "seen" by negating the value at their index
        for x in nums:
            index = abs(x) - 1
            if nums[index] > 0:
                nums[index] *= -1
        
        # Step 2: Any index still positive was never visited
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

