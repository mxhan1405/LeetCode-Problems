class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        # Store the original color we need to replace
        start_color = image[sr][sc]
        
        # If the starting pixel is already the target color, no changes are needed
        if start_color == color:
            return image
        
        rows, cols = len(image), len(image[0])
        
        def dfs(r, c):
            # Check if current position is within bounds and matches the original color
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != start_color:
                return
            
            # Update the color
            image[r][c] = color
            
            # Recursively fill 4-directional neighbors
            dfs(r + 1, c) # Down
            dfs(r - 1, c) # Up
            dfs(r, c + 1) # Right
            dfs(r, c - 1) # Left
            
        dfs(sr, sc)
        return image

