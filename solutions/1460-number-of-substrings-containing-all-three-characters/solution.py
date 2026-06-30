class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Dictionary to keep track of the count of 'a', 'b', and 'c'
        counts = {'a': 0, 'b': 0, 'c': 0}
        
        result = 0
        left = 0
        n = len(s)
        
        # Expand the right boundary of the window
        for right in range(n):
            counts[s[right]] += 1
            
            # Shrink the window from the left as long as it contains at least one 'a', 'b', and 'c'
            while counts['a'] > 0 and counts['b'] > 0 and counts['c'] > 0:
                # If the window from 'left' to 'right' is valid, 
                # then all substrings starting from 'left' up to the end of the string are also valid.
                result += (n - right)
                
                # Remove the character at the left pointer and move it forward
                counts[s[left]] -= 1
                left += 1
                
        return result

