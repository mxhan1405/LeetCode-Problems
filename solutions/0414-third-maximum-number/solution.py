class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a=set(nums)
        s=sorted(a)
        if len(s)<3:
            return max(s)

        else:
            return s[-3]
            
