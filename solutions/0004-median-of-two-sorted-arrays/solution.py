class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ar3=nums1+nums2
        n=len(ar3)
        ar3.sort()
        mid= n//2
        if n%2==0:
            return float(ar3[mid]+ar3[mid-1])/2
        else:
            return float(ar3[mid])
