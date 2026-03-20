class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        # 1. Find the duplicate using a set
        seen = set()
        duplicate = -1
        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)
        
        # 2. Use the sum of 1 to n to find the missing number
        # Actual Sum - Duplicate + Missing = Expected Sum
        # Therefore: Missing = Expected Sum - (Actual Sum - Duplicate)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        
        missing = expected_sum - (actual_sum - duplicate)
        
        return [duplicate, missing]

