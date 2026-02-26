class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        
        # Iterate from right to left, skipping the first bit
        for i in range(len(s) - 1, 0, -1):
            # Current value is the bit plus any carry from the right
            digit = int(s[i]) + carry
            
            if digit == 1:
                # If odd: Add 1 (1 step) + Divide by 2 (1 step) = 2 steps
                steps += 2
                carry = 1
            else:
                # If even: Just divide by 2 = 1 step
                steps += 1
                
        # Final carry added to the original leading '1'
        return steps + carry

