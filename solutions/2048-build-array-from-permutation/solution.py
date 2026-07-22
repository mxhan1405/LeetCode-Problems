class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        a=[]
        for i in range(0,len(nums)):
            b=nums[i]
            a.append(nums[b])
        return a
