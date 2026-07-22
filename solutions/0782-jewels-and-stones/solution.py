class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c=0
        for s in jewels:
            c=c+stones.count(s)
        return c
