class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        for i in range(len(nums)):
            a.append(nums[i])
            b.append(nums[i])
        c=a+b
        return c
        
