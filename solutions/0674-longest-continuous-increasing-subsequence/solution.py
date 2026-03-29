class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # ans: overall maximum length found
        # count: length of the current strictly increasing sequence
        ans = count = 1
        
        for i in range(1, len(nums)):
            # Check if strictly increasing
            if nums[i] > nums[i - 1]:
                count += 1
                # Update global maximum
                ans = max(ans, count)
            else:
                # Sequence broken; reset for a new one starting at current element
                count = 1
                
        return ans

