class Solution:
    def __init__(self):
        self.ROWS = 0
        self.COLUMNS = 0

    def mapIsland(self, grid, r, c, visited):
        if (r == -1 or r == self.ROWS
        or c == -1 or c == self.COLUMNS
        or grid[r][c] == "0"
        or (r, c) in visited):
            return

        visited.add((r, c))
        self.mapIsland(grid, r + 1, c, visited)
        self.mapIsland(grid, r - 1, c , visited)
        self.mapIsland(grid, r, c + 1, visited)
        self.mapIsland(grid, r, c - 1, visited)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.ROWS = len(grid)
        self.COLUMNS = len(grid[0])
        visited = set()
        ret = 0

        for row in range(0, self.ROWS):
            for col in range(0, self.COLUMNS):
                if (grid[row][col] == "1" 
                and (row, col) not in visited):
                    ret += 1
                    self.mapIsland(grid, row, col, visited)

        return ret
        