import math

class Solution:
    def findGCD(self, nums: list[int]) -> int:
        # Find the smallest and largest numbers in a single pass or via built-ins
        smallest = min(nums)
        largest = max(nums)
        
        # Calculate and return the greatest common divisor
        return math.gcd(smallest, largest)

