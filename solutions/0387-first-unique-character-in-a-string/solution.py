class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        f = s[0]
        if f not in s[1:]:
            return 0
        for i in range(1, len(s)):
            if s.count(s[i]) == 1:
                return i
                
        return -1

