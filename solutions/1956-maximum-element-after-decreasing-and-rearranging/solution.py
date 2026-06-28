class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        # Step 1: Sort the array to process elements in ascending order
        arr.sort()
        
        # Condition 1: The first element must be 1
        arr[0] = 1
        
        # Step 2: Ensure adjacent element differences are at most 1
        for i in range(1, len(arr)):
            arr[i] = min(arr[i], arr[i - 1] + 1)
            
        # The largest valid element will naturally bubble up to the end
        return arr[-1]

