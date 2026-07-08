class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        ar =[]
        for i in range(len(nums)):
            if nums[i]==val:
                count = count +1
            else:
                ar.append(nums[i])
        for i in range(len(ar)):
            nums[i] = ar[i]
            
        return len(nums) - count
