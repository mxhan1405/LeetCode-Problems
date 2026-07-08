class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Loop backwards through the digits
        for i in reversed(range(len(digits))):
            if digits[i] < 9:
                digits[i] += 1
                return digits  # Done! Return immediately
            
            digits[i] = 0  # It was a 9, so turn it to 0 and carry over
            
        # If all digits were 9s (e.g., 99 -> 00), put a 1 at the front
        return [1] + digits

