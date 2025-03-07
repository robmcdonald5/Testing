class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best_output = float('inf')
        left = 0
        current_best = 0
        
        for right in range(len(nums)):
            current_best += nums[right]

            while current_best >= target:
                best_output = min(best_output, right - left+1)

                current_best -= nums[left]
                left+=1

        return best_output if best_output != float('inf') else 0