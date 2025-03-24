class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        base_max = nums[0]
        best_max = base_max

        for i in range(1, len(nums)):
            base_max = max(nums[i], base_max+nums[i])

            best_max = max(best_max, base_max)

        return best_max