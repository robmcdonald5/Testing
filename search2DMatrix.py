class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        for row in matrix:
            left, right = 0, len(matrix[0])-1
            while left <= right:
                mid = (left+right) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    left = mid+1
                else:
                    right = mid-1

        return False