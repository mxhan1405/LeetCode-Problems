class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        a=[]
        count=0
        a=sorted(heights)
        for i in range(len(heights)):
            if a[i]!=heights[i]:
                count=count+1
        return count
