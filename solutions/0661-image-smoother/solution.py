class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        rows, cols = len(img), len(img[0])
        # Create a result matrix to store smoothed values
        res = [[0] * cols for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                total_sum = 0
                count = 0
                
                # Check all 9 possible positions in the 3x3 grid
                for i in range(max(0, r - 1), min(rows, r + 2)):
                    for j in range(max(0, c - 1), min(cols, c + 2)):
                        total_sum += img[i][j]
                        count += 1
                
                # Apply integer division (rounds down)
                res[r][c] = total_sum // count
                
        return res

