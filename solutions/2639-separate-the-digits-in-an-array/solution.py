class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        n=[]
        m=list(nums)
        for i in range(len(m)):
            if nums[i]<10:
                n.append(nums[i])
            else:
                for ch in str(nums[i]):
                    n.append(int(ch))
        return n
