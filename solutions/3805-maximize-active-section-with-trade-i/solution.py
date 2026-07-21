from itertools import groupby

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # Count the original number of '1's in s
        initial_ones = s.count('1')
        
        # Augment the string as specified
        t = '1' + s + '1'
        
        # Group into blocks of (character, run_length)
        # e.g., "1011" -> [('1', 1), ('0', 1), ('1', 2)]
        blocks = [(char, len(list(group))) for char, group in groupby(t)]
        
        max_gain = 0
        
        # Look for any block of '1's completely surrounded by '0's
        for i in range(1, len(blocks) - 1):
            char, length = blocks[i]
            if char == '1':
                # Check if both adjacent blocks are '0's
                if blocks[i-1][0] == '0' and blocks[i+1][0] == '0':
                    # The gain is the total number of zeros flipped into ones
                    current_gain = blocks[i-1][1] + blocks[i+1][1]
                    if current_gain > max_gain:
                        max_gain = current_gain
                        
        return initial_ones + max_gain

