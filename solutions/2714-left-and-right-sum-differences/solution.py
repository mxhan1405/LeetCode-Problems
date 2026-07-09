class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum=[]
        rightsum=[]
        left_total = 0
        for i in range(len(nums)):
            leftsum.append(left_total)
            left_total += nums[i]
        right_total = 0
        for i in range(len(nums) - 1, -1, -1):
            rightsum.append(right_total)
            right_total += nums[i]   
        rightsum.reverse()
        answer = []
        for i in range(len(nums)):
            difference = abs(leftsum[i] - rightsum[i])
            answer.append(difference)
            
        return answer
