class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        max = 1

        if n == 1:
            return nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                max+=1
            else:
                max=1
            if max > n//2:
                return nums[i]