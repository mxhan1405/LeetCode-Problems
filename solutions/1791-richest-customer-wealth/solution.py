class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m=0
        for account in accounts:
            rich=0
            for c in account:
                rich+=c
            m=max(m,rich)
        return m
