class Solution:
    def fourSum(self, nums, target):
        nums.sort()  # Step 1: Sort to handle duplicates and use two pointers
        n = len(nums)
        ans = []
        
        # Step 2: Iterate through the first element
        for i in range(n - 3):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Step 3: Iterate through the second element
            for j in range(i + 1, n - 2):
                # Skip duplicates for the second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Step 4: Two pointers for the remaining two elements
                left, right = j + 1, n - 1
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if current_sum == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates for the third and fourth elements
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
        return ans

