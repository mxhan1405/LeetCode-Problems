class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        n=0
        for i in range(len(nums)):
            n=len(str(nums[i]))
            if n%2==0:
                count+=1
        return count
