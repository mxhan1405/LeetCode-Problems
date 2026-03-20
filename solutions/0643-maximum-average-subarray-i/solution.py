class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Initial sum of the first k elements
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Slide the window from index k to the end
        for i in range(k, len(nums)):
            # Add the next element and subtract the one that's leaving
            current_sum += nums[i] - nums[i - k]
            
            if current_sum > max_sum:
                max_sum = current_sum
        
        # Return the max sum divided by k to get the average
        return max_sum / k

