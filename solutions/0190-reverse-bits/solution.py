class Solution:
    def reverseBits(self, n: int) -> int:
        c = format(n, '032b') 
        d = "".join(reversed(c)) 
        
        b = int(d, 2) 
        return b

