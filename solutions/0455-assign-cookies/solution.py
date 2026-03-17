class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        
        child_i = 0
        cookie_j = 0
        
        # While there are children left to feed AND cookies left to give
        while child_i < len(g) and cookie_j < len(s):
            # If the current cookie can satisfy the current child
            if s[cookie_j] >= g[child_i]:
                child_i += 1  # Move to the next child
            
            # Move to the next cookie regardless
            cookie_j += 1
            
        return child_i

