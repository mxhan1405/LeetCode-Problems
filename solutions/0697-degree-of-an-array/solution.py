class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        first, last, count = {}, {}, {}
        
        for i, x in enumerate(nums):
            if x not in first: 
                first[x] = i
            last[x] = i
            count[x] = count.get(x, 0) + 1
            
        # The degree is the maximum frequency of any element
        degree = max(count.values())
        ans = len(nums)
        
        for x in count:
            if count[x] == degree:
                # Calculate the span for each candidate element
                ans = min(ans, last[x] - first[x] + 1)
                
        return ans

