class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            s = str(num)
            l = list(s)
            sum = 0
            for i in range(len(l)):
                sum = sum + int(l[i])
            k = str(sum)
            lk = list(k)
            total = 0
            for i in range(len(lk)):
                total = total + int(lk[i])
            num = total
            
        return num

