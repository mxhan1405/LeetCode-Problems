class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # Using Python's bit_count (3.10+) or bin(x).count('1')
        return sorted(arr, key=lambda x: (x.bit_count(), x))

