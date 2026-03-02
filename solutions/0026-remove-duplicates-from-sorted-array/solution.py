class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # i is the pointer for the last unique element found
        i = 0
        
        # j is the explorer pointer
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
                
        return i + 1

