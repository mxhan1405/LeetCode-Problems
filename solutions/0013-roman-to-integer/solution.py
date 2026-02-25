class Solution:
    def romanToInt(self, s: str) -> int:
        # 1. Map symbols to values (O(1) lookup)
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        # 2. Start from the last character's value
        total = roman_map[s[-1]]
        
        # 3. Iterate backwards from the second-to-last character
        for i in range(len(s) - 2, -1, -1):
            # If current value < next value, subtract (subtractive rule: IV, XC, etc.)
            if roman_map[s[i]] < roman_map[s[i+1]]:
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]
                
        return total

