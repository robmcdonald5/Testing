class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        current_val = n

        while current_val != 1 and current_val not in seen:
            seen.add(current_val)

            next_val = 0
            while current_val > 0:
                digit = current_val % 10
                next_val += digit ** 2
                current_val //= 10
            current_val = next_val

        return current_val == 1
