class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first=strs[0]
        last=strs[-1]
        ah=""
        for i in range(len(first)):
            if first[i]==last[i]:
                ah+=first[i]
            else:
                break
        return ah
