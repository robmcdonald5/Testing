from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        LP = m-1
        RP = n-1
        MP = m+n-1
        print(LP)
        print(RP)
        print(MP)

        while LP >= 0 and RP >= 0:
            if nums1[LP] > nums2[RP]:
                nums1[MP] = nums1[LP]
                LP-=1
            else:
                nums1[MP] = nums2[RP]
                RP-=1
            MP-=1
        while RP >= 0:
            nums1[MP] = nums2[RP]
            RP-=1
            MP-=1

# Test case 1: Basic merge
nums1 = [1, 3, 5, 0, 0, 0]
m = 3
nums2 = [2, 4, 6]
n = 3

print(f"Test Case 1 - Before: nums1 = {nums1}, nums2 = {nums2}")
solution = Solution()
solution.merge(nums1, m, nums2, n)
print(f"Test Case 1 - After: nums1 = {nums1}")

# Test case 2: When nums2 has smaller elements
nums1 = [4, 5, 6, 0, 0, 0]
m = 3
nums2 = [1, 2, 3]
n = 3

print(f"\nTest Case 2 - Before: nums1 = {nums1}, nums2 = {nums2}")
solution.merge(nums1, m, nums2, n)
print(f"Test Case 2 - After: nums1 = {nums1}")

# Test case 3: When nums1 is empty
nums1 = [0, 0, 0]
m = 0
nums2 = [1, 2, 3]
n = 3

print(f"\nTest Case 3 - Before: nums1 = {nums1}, nums2 = {nums2}")
solution.merge(nums1, m, nums2, n)
print(f"Test Case 3 - After: nums1 = {nums1}")

# Test case 4: When nums2 is empty
nums1 = [1, 2, 3]
m = 3
nums2 = []
n = 0

print(f"\nTest Case 4 - Before: nums1 = {nums1}, nums2 = {nums2}")
solution.merge(nums1, m, nums2, n)
print(f"Test Case 4 - After: nums1 = {nums1}")