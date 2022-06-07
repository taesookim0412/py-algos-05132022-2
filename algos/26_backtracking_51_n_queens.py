# ......

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.boards = []
        self.n = n
        currentBoard = [[0 for _ in range(n)] for _ in range(n)]
        self.backtrack(currentBoard, 0, 0, 0, set(), set())

    def backtrack(self, board, queenCount, row, col, diags, antiDiags):
        if queenCount == self.n:
            self.boards.append(board)
        for _ in range(col):
            currDiagonal = row - col
            currAntiDiagonal = row + col

            if currDiagonal not in diags and currAntiDiagonal not in antiDiags

