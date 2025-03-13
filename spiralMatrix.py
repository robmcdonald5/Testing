class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        path = []
        rows, cols = len(matrix), len(matrix[0])

        top = 0
        bottom = rows - 1
        left = 0
        right = cols - 1
        # 0 = right, 1 = down, 2 = left, 3 = up
        direction = 0

        while top <= bottom and left <= right:
            if direction == 0:
                for i in range(left, right + 1):
                    path.append(matrix[top][i])
                top += 1
            elif direction == 1:
                for i in range(top, bottom + 1):
                    path.append(matrix[i][right])
                right -= 1
            elif direction == 2:
                for i in range(right, left - 1, -1):
                    path.append(matrix[bottom][i])
                bottom -= 1
            elif direction == 3:
                for i in range(bottom, top - 1, -1):
                    path.append(matrix[i][left])
                left += 1

            direction = (direction + 1) % 4

        return path