class Solution:
    def passwordStrength(self, p: str) -> int:
        t=0
        k=set(p)
        for i in k:
            if i.islower():
                t=t+1
            elif i.isupper():
                t=t+2
            elif i.isdigit():
                t=t+3
            elif not i.isalnum():
                t=t+5
        return t  
            
