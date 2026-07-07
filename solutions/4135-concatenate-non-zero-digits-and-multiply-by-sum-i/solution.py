class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = str(n)
        ns = ""
        for i in range(len(s)):
            if s[i] != '0':
                ns += s[i]
        if ns == "":
            return 0
        x = int(ns)
        
        digit_sum = 0
        for i in range(len(ns)):
            digit_sum += int(ns[i])
        return x * digit_sum

