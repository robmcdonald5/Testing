class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        if len(s) % 2 != 0:
            return False
        
        stack = []

        special_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if not stack or stack.pop() != special_map[char]:
                    return False

        return len(stack) == 0