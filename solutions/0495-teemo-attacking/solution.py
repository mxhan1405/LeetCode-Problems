class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        if not timeSeries:
            return 0
        
        total_time = 0
        # Iterate through attacks, comparing the current one to the next
        for i in range(len(timeSeries) - 1):
            # Calculate how long Ashe stays poisoned before the next attack
            # It's either the full duration OR the time until the next hit
            total_time += min(timeSeries[i + 1] - timeSeries[i], duration)
        
        # The last attack always lasts for the full duration
        return total_time + duration

