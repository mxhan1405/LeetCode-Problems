class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        i = 0
        n = len(bits)
        
        # Traverse until the second-to-last element
        while i < n - 1:
            if bits[i] == 1:
                # If we see a 1, skip 2 positions (two-bit character)
                i += 2
            else:
                # If we see a 0, skip 1 position (one-bit character)
                i += 1
        
        # If we land exactly on the last index, it's a one-bit character
        return i == n - 1

