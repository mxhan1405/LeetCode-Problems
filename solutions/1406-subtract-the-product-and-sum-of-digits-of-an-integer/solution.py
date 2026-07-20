class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a=0
        m=1
        for i in str(n):
            a=a+int(i)
            m=m*int(i)
        return m-a
