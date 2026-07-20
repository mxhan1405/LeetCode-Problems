class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        es=0
        ds=0

        for num in nums:
            for j in str(num):
                ds=ds+int(j)
            es=es+num
        return es-ds
