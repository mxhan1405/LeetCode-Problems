class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        a=[]
        b=[]
        a=sorted(nums1)
        b=sorted(nums2)
        c=b[-1]-a[-1]
        return c
