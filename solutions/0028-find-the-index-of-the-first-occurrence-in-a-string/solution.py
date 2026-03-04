class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # These lines must be indented inside the function
        h_len = len(haystack)
        n_len = len(needle)
        
        # This loop must also be indented
        for i in range(h_len - n_len + 1):
            # This if-statement is indented inside the loop
            if haystack[i : i + n_len] == needle:
                return i
        
        # This return is outside the loop but inside the function
        return -1

