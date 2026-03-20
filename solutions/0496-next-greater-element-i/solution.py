class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Dictionary to store {number: its_next_greater_element}
        mapping = {}
        stack = []
        
        # Iterate through nums2 to find next greater elements
        for num in nums2:
            # While the current number is greater than the stack's top,
            # it is the "next greater" for that top element
            while stack and num > stack[-1]:
                mapping[stack.pop()] = num
            stack.append(num)
            
        # For any elements left in the stack, there was no next greater
        while stack:
            mapping[stack.pop()] = -1
            
        # Map the results back to the order requested in nums1
        return [mapping[num] for num in nums1]

