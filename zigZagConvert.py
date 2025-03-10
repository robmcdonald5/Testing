class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= 1 or numRows <= 1:
            return s
        
        str_rows = [""] * numRows
        #str_rows[0] += str[0]

        i = 0
        while i in range(len(s)):
            