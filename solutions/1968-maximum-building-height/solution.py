class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        # Step 1: Add the structural boundaries
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])
        
        # Sort restrictions by building ID
        restrictions.sort()
        
        # Step 2: Forward pass (Left to Right)
        for i in range(1, len(restrictions)):
            dist = restrictions[i][0] - restrictions[i-1][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i-1][1] + dist)
            
        # Step 3: Backward pass (Right to Left)
        for i in range(len(restrictions) - 2, -1, -1):
            dist = restrictions[i+1][0] - restrictions[i][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1] + dist)
            
        # Step 4: Calculate the absolute max height between adjacent bounds
        max_height = 0
        for i in range(1, len(restrictions)):
            x1, h1 = restrictions[i-1]
            x2, h2 = restrictions[i]
            # Mathematical formula to find the peak between x1 and x2
            peak = (h1 + h2 + (x2 - x1)) // 2
            max_height = max(max_height, peak)
            
        return max_height

