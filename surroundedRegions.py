class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def DFS(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return

            board[i][j] = 'E' #E represents escaped

            DFS(i+1, j)
            DFS(i-1, j)
            DFS(i, j+1)
            DFS(i, j-1)

        for j in range(n):
            DFS(0, j)
            DFS(m-1, j)
        for i in range(1, m-1):
            DFS(i, 0)
            DFS(i, n-1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'E':
                    board[i][j] = 'O'