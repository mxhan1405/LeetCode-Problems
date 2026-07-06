class Solution(object):
    def removeCoveredIntervals(self, intervals):
        # Sort by start point ascending, then by end point descending
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        remaining_count = 0
        current_end = 0
        
        for interval in intervals:
            end = interval[1]
            # If the end extends further, it is not covered
            if end > current_end:
                remaining_count += 1
                current_end = end
                
        return remaining_count

