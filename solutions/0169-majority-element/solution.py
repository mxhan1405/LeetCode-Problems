class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for n in nums:
            # If count drops to 0, we pick a new candidate
            if count == 0:
                candidate = n
            
            # Increment count if current number matches candidate, else decrement
            count += (1 if n == candidate else -1)

        return candidate

