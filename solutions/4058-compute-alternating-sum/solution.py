class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        neg = 1
        res = 0
        for x in nums:
            res = res + (neg*x)
            neg = neg*-1
        return res
