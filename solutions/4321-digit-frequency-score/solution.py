class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        sum=0
        for k in str(n):
            sum+=int(k)
        return sum
