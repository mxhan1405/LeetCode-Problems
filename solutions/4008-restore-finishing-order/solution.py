class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        a=[]
        for n in order:
            if n in friends:
                a.append(n)
        return a
