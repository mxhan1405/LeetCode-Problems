class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        k=""
        if len(words)!= len(s):
            return False
        else:
            for i in range(len(words)):
                if words[i][0]!=s[i]:
                    return False
            return True
