class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)
        i=0

        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
                k-=1
            else:
                i+=1
        
        return k