class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alp="abcdefghijklmnopqrstuvwxyz"
        s=sentence.lower()
        l=set(s)
        if len(l)==26:
            return True
        else :
            return False
