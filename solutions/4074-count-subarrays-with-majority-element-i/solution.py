class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        """
        Counts the total number of subarrays where 'target' is the majority element.
        """
        n = len(nums)
        subarray_count = 0
        
        # Outer loop sets the start index of the subarray
        for start in range(n):
            target_frequency = 0
            
            # Inner loop expands the subarray to the right
            for end in range(start, n):
                if nums[end] == target:
                    target_frequency += 1
                
                current_length = end - start + 1
                
                # 'target' is the majority element if its frequency is strictly 
                # greater than half the length of the subarray
                if target_frequency > (current_length // 2):
                    subarray_count += 1
                    
        return subarray_count

