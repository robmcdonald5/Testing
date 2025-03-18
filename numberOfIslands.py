class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        count = 0
        rows, cols = len(grid), len(grid[0])

        def DFS(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return

            grid[r][c] = '0'

            DFS(r+1, c)
            DFS(r-1, c)
            DFS(r, c+1)
            DFS(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    DFS(r, c)

        return count