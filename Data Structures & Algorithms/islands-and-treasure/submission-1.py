from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])
        todo = deque()

        for i in range(0, ROWS):
            for j in range(0, COLS):
                if grid[i][j] == 0:
                    todo.append((i, j))

        dist = 1
        while len(todo) > 0:
            for i in range(len(todo)):
                r, c = todo.popleft()
                steps = [[0, -1], [0, 1], [-1, 0], [1, 0]]

                for dr, dc in steps:
                    nr, nc = r + dr, c + dc
                    if (nr >= 0 and nr < ROWS and
                    nc >= 0 and nc < COLS and 
                    dist < grid[nr][nc]):
                        grid[nr][nc] = dist
                        todo.append((nr, nc))
            dist += 1


        