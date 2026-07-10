class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a=[]
        f=[]
        l=len(candies)
        m=max(candies)
        for i in range(l):
            a.append(extraCandies + candies[i])
        for i in range(l):
            if a[i]>=m:
                f.append(True)
            else:
                f.append(False)
        return f
