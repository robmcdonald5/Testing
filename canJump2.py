class Solution:
    def jump(self, nums: List[int]) -> int:
        min_jump = 0
        slice_min = 0
        slice_max = nums[0]

        i=0
        while i < len(nums):
            if nums[i] >= len(nums)-1:
                min_jump+=1
                return min_jump
            elif max(nums[slice_min:slice_max]) > nums[i]:
                min_jump+=1
            