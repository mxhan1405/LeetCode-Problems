class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters 
        using an optimized sliding window protocol.
        
        Time Complexity: O(N) - Single pass iteration.
        Space Complexity: O(min(M, N)) - M is the character set size (ASCII/symbols).
        """
        # Dictionary to store the most recent index of each character
        char_map = {}
        max_length = 0
        left = 0
        
        for right, char in enumerate(s):
            # If the character is found inside our current valid window,
            # instantly jump the left boundary right past its previous location.
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            
            # Record or update the active index position of the character
            char_map[char] = right
            
            # Calculate the current sliding window size and check for a new maximum
            max_length = max(max_length, right - left + 1)
            
        return max_length

