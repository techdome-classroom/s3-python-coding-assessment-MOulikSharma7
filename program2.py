class Solution(object):
    class Solution:
    def romanToInt(self, s: str) -> int:
        # Define a mapping of Roman numerals to their integer values
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        
        # Initialize the total integer value
        total = 0
        
        # Iterate over the string s
        for i in range(len(s)):
            # Check if we should apply the subtraction rule
            if i + 1 < len(s) and roman_values[s[i]] < roman_values[s[i + 1]]:
                # Subtract the current value
                total -= roman_values[s[i]]
            else:
                # Add the current value
                total += roman_values[s[i]]
        
        return total




