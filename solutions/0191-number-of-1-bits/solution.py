class Solution:
    def hammingWeight(self, n: int) -> int:
        b=format(n,'b')
        c=0
        for i in b:
            if i=='1':
                c+=1
        return c
