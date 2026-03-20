class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_streak = 0
        current_streak = 0
        
        for num in nums:
            if num == 1:
                current_streak += 1
                # Update max_streak if the current one is longer
                if current_streak > max_streak:
                    max_streak = current_streak
            else:
                # Reset the counter when we hit a 0
                current_streak = 0
                
        return max_streak


