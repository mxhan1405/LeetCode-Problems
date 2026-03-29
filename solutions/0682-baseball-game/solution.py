class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        
        for op in operations:
            if op == "+":
                # Add a new score that is the sum of the previous two scores
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                # Add a new score that is double the previous score
                stack.append(2 * stack[-1])
            elif op == "C":
                # Invalidate the previous score, removing it from the record
                stack.pop()
            else:
                # The operation is an integer; record it as a new score
                stack.append(int(op))
        
        # Return the sum of all scores in the record
        return sum(stack)

