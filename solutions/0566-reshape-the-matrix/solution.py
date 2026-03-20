class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        
        # Check if reshape is possible
        if m * n != r * c:
            return mat
        
        # Flatten the matrix into a single list
        flat = [val for row in mat for val in row]
        
        # Build the new matrix by taking slices of length c
        return [flat[i * c : (i + 1) * c] for i in range(r)]

