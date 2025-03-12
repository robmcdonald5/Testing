class Solution:
    def trap(self, height: List[int]) -> int:
        current_vol = 0
        max_pos = height[0]

        for i in range(len(height)):
            if height[i] > max_pos:
                max_pos = height[i]

        left_pointer = max_pos-1
        right_pointer = max_pos+1

        right_max = max_pos
        while left_pointer >= 0:
            if height[right_max] == height[left_pointer]:
                left_pointer -= 1
                right_max -= 1
            
            