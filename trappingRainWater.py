class Solution:
    def trap(self, height: List[int]) -> int:
        left_start = 0
        right_start = len(height)-1

        for i in range(len(height)):
            if height[i] == 0:
                left_start+=1
                continue
            break
        for i in range(right_start-1, -1, -1):
            if height[i] == 0:
                right_start-=1
                continue
            break

        current_volume = 0

        for i in range(left_start, len(height)):
            
        for i in range(right_start, -1, -1):