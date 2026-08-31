class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])
        visited = set()

        def dfs(r, c, i):
            if i >= len(word):
                return True

            if r < 0 or r >= ROW or c < 0 or c >= COL:
                return False

            if board[r][c] != word[i] or (r, c) in visited:
                return False

            visited.add((r, c))

            result = dfs(r + 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1) or dfs(r - 1, c, i + 1)

            visited.remove((r, c))

            return result

        for i in range(ROW):
            for j in range(COL):
                if dfs(i, j, 0):
                    return True

        return False