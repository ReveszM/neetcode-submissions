from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        todo = deque([(0, 0)])
        visited = set([(0, 0)])
        if grid[0][0] != 0:
            return -1

        length = 1
        while len(todo) > 0:
            for i in range(len(todo)):
                r, c = todo.popleft()
                if r == ROWS - 1 and c == COLS -1:
                    return length

                steps = [[0, 1], [0, -1], 
                        [1, 0], [1, 1], [1, -1],
                        [-1, 0], [-1, 1], [-1, -1]]
                for dr, dc in steps:
                    nr, nc = r + dr, c + dc

                    if (nr < 0 or nr > ROWS - 1
                    or nc < 0 or nc > COLS - 1
                    or grid[nr][nc] != 0
                    or (nr, nc) in visited):
                        continue
                    
                    todo.append((nr, nc))
                    visited.add((nr, nc))
            length += 1
        return -1
        