class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sToT, tToS = {}, {}

        for i in range(len(s)):
            sC, tC = s[i], t[i]

            if ((sC in sToT and sToT[sC] != tC) or (tC in tToS and tToS[tC] != sC)):
                return False
            
            sToT[sC] = tC
            tToS[tC] = sC

        return True