class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = min(len(s) for s in strs)
        best_common = ""

        for i in range(min_length):
            current_char = strs[0][i]

            if all(s[i] == current_char for s in strs):
                best_common += current_char
            else:
                break

        return best_common