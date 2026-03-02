class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # k will be the index where we place the next element != val
        k = 0
        
        for i in range(len(nums)):
            # If the current element is not the target value
            if nums[i] != val:
                # Move it to the 'k' position and increment k
                nums[k] = nums[i]
                k += 1
                
        # k is the count of elements not equal to val
        return k

