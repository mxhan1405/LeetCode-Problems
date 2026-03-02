class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        
        # Start from the end of the list and move backwards
        for i in range(n - 1, -1, -1):
            # If the current digit is less than 9, just increment and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # If the digit is 9, it becomes 0 (carry the 1 to the next iteration)
            digits[i] = 0
            
        # If we exit the loop, it means we had a carry for the most significant digit
        # (e.g., [9, 9] -> [0, 0]). We need to add 1 at the beginning.
        return [1] + digits

