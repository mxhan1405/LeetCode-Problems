class Solution:
    def sumOfMultiples(self, n: int) -> int:
        a=[]
        s=0
        for i in range(1,n+1):
            if i%3==0:
                a.append(i)
            elif i%5==0:
                a.append(i)
            elif i%7==0:
                a.append(i)
        for i in range(len(a)):
            s=s+a[i]
        return s
