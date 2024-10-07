class Solution(object):
    def isValid(s: str) -> bool:
    # Stack to keep track of opening brackets
        stack = []
        
        # Dictionary to match closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        # Traverse each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top element from the stack (if stack is not empty) or assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the top element doesn't match the corresponding opening bracket, return False
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
        
        # Return True if the stack is empty (all brackets matched), otherwise False
        return not stack









    



  

