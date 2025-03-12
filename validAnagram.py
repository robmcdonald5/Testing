class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False

        for i in range(len(t)):
            ch = t[i]
            if ch in s:
                s = s.replace(ch, '', 1)
            else:
                return False

        return True