class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        a=sorted(nums)
        d=sorted(nums,reverse=True)
        for i in range(len(nums)):
            if nums==a:
                return True
            elif nums==d:
                return True
            else:
                return False
