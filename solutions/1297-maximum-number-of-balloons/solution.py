from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Step 1: Count occurrences of each character
        counts = Counter(text)
        
        # Step 2: Return the maximum number of words formed
        return min(
            counts['b'],
            counts['a'],
            counts['l'] // 2,
            counts['o'] // 2,
            counts['n']
        )

