class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s=sorted(nums)
        a=[]
        ar=0
        sum=0
        for i in range(len(nums)):
            if nums[i]>=10:
                a.append(nums[i])
                nums[i]=0
            sum+=nums[i]
        for i in range(len(a)):
            ar+=a[i]
        if sum!=ar: 
            return True
        else :
            return False
