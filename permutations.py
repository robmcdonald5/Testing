class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output_combos = []

        def backtrack(current, remaining):
            if not remaining:
                output_combos.append(current[:])
                return
            
            for i in range(len(remaining)):
                current.append(remaining[i])

                backtrack(current, remaining[:i] + remaining[i+1:])

                current.pop()

        backtrack([], nums)

        return output_combos