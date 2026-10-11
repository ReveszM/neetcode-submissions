from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        for i in range(0, ROWS):
            for j in range(0, COLS):
                if (grid[i][j] == 1 and
                (i, j) not in visited):
                    todo = deque([(i, j)])
                    visited.add((i, j))
                    area = 0

                    while len(todo) > 0:
                        area += 1
                        r, c = todo.popleft()

                        steps = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                        for cur_step in steps:
                            nr = r + cur_step[0]
                            nc = c + cur_step[1]
                            if (nr >= 0 and nr < ROWS and 
                            nc >= 0 and nc < COLS and 
                            (nr, nc) not in visited and
                            grid[nr][nc] == 1):
                                todo.append((nr, nc))
                                visited.add((nr, nc))
                    res = max(res, area)

        return res
        