class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        b=[]
        a = ",".join(map(str, nums))
        b=a.replace('-','')
        str_list = b.split(",")
        squared_nums = [int(x) ** 2 for x in str_list]
        return sorted(squared_nums)
