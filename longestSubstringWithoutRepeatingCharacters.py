class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        longest_substring = s[0]
        max_len = 1
        for i in range(1, len(s)):
            if s[i] not in longest_substring:
                longest_substring += s[i]
                if len(longest_substring) > max_len:
                    max_len = len(longest_substring)
            else:
                duplicate_index = longest_substring.index(s[i])
                longest_substring = longest_substring[duplicate_index + 1:] + s[i]

        return max_len