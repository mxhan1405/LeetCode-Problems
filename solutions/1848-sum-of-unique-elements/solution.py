class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        unique = []
        for x in nums:
            if nums.count(x) == 1:
                unique.append(x)
        return sum(unique)

