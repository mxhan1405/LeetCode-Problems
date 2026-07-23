class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        d={}
        while n>0:
            t=n%10
            if t not in d.keys():
                d[t]=1
            else:
                d[t]+=1
            n=n//10
        ans=0
        for k in d.keys():
            ans+=(k*d[k])
        return ans



