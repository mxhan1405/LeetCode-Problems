class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        nd=0
        dd=0
        for i in range(1,n+1):
            if i%m==0:
                dd=dd+i
            else:
                nd=nd+i
        return nd-dd
