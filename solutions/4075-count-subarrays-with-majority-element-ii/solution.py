class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        # Shift offset to handle negative prefix sums in Fenwick Tree index range
        offset = n + 1
        # Size of the BIT array to accommodate prefix sums from -n to n
        bit_size = 2 * n + 2
        bit = [0] * bit_size

        def update(idx: int, delta: int):
            while idx < bit_size:
                bit[idx] += delta
                idx += idx & (-idx)

        def query(idx: int) -> int:
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s

        # Base case: before processing any elements, prefix sum is 0
        update(0 + offset, 1)
        
        result = 0
        current_prefix_sum = 0
        
        for num in nums:
            # Transform: target element acts as +1, any other element acts as -1
            if num == target:
                current_prefix_sum += 1
            else:
                current_prefix_sum -= 1
            
            # Count how many previous prefix sums are strictly less than current_prefix_sum
            result += query(current_prefix_sum + offset - 1)
            
            # Store the current prefix sum in the Fenwick Tree
            update(current_prefix_sum + offset, 1)
            
        return result

