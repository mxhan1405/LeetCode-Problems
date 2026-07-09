class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        a=[]
        b=[]
        d=[]
        for i in range(len(nums)):
            a.append(nums[i])
            b.append(nums[i])
        d=list(reversed(b))
        c=a+d
        return c
        
