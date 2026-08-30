class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0

        rows = len(grid)
        cols = len(grid[0]) 

        def dfs(r, c):
            if r >= rows or c >= cols or r < 0 or c < 0 or grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            return 1 + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    result = max(result, dfs(r, c))

        return result

        