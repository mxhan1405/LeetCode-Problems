class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        # 1. Sort the array in ascending order
        # 2. Use slicing [::2] to pick elements at indices 0, 2, 4...
        # 3. Return the sum of those elements
        return sum(sorted(nums)[::2])

