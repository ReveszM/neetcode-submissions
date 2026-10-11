from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        todo = deque()
        for r in range(0, ROWS):
            for c in range(0, COLS):
                if grid[r][c] == 2:
                    todo.append((r, c))

        m = 0
        change = False
        while len(todo) > 0:
            for i in range(len(todo)):
                r, c = todo.popleft()

                steps = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in steps:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS 
                    and 0 <= nc < COLS
                    and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        todo.append((nr, nc))
                        change = True
            if change:
                m += 1
                change = False

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return m

        