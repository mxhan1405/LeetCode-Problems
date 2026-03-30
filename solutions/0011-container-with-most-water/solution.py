class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Initialize two pointers at the start and end of the array
        left, right = 0, len(height) - 1
        max_water = 0
        
        while left < right:
            # Calculate the current width between pointers
            width = right - left
            # The container's height is limited by the shorter of the two lines
            h = min(height[left], height[right])
            
            # Update max_water if the current area is larger
            max_water = max(max_water, width * h)
            
            # Move the pointer pointing to the shorter line to seek a taller one
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water

