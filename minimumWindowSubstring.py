s = "ADOBECODEBANC"
t = "ABC"

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s

        shortest_substring = ""

        for i in range(len(s)):
            current_substring = ""
            if s[i] not in t:
                continue
            for j in range(i, len(s)):
                if s[j] in t:
                    current_substring = current_substring + s[j]
                    if len(current_substring) == len(t):
                        break
                print(current_substring)
            if len(current_substring) < len(shortest_substring):
                shortest_substring = current_substring

        return shortest_substring
