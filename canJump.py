class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_j = 0

        for i in range(len(nums)):
            if i > max_j:
                return False
            
            max_j = max(max_j, i + nums[i])

            if max_j >= len(nums) - 1:
                return True
        
        return max_j >= len(nums) - 1