class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        output = []
        digitDict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(index, current_str):
            if index == len(digits):
                output.append(current_str)
                return

            current_digit = digits[index]
            letters = digitDict[current_digit]

            for letter in letters:
                backtrack(index+1, current_str+letter)

        backtrack(0, "")
        return output