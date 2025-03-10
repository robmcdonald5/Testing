class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        currentWord = ""
        i = len(s) - 1
        while i >= 0:
            if s[i] == " ":
                i-=1
                continue
            else:
                i-=1
                break

        while i >= 0:
            if s[i] == " ":
                break
            else:
                currentWord = currentWord+s[i]
                i-=1

        return len(currentWord)+1