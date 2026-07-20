class Solution:
    def separateDigits(self, n: List[int]) -> List[int]:
        r=[]
        for i in n:
            s=str(i)
            for j in s:
                r.append(int(j))
        return r
