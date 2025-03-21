class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output_combos = []

        def backtrack(start, curr_combination):
            if len(curr_combination) == k:
                output_combos.append(curr_combination[:])
                return
            
            for i in range(start, n+1):
                curr_combination.append(i)

                backtrack(i+1, curr_combination)
                curr_combination.pop()

        backtrack(1, [])

        return output_combos