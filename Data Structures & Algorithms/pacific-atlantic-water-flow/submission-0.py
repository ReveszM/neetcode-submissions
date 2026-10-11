from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        
        reachPacific = set()
        todo = deque()
        for i in range(ROWS):
            todo.append((i, 0))
            reachPacific.add((i, 0))
        for i in range(1, COLS):
            todo.append((0, i))
            reachPacific.add((0, i))
        
        while len(todo) > 0:
            for i in range(len(todo)):
                r, c = todo.popleft()
                steps = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for dr, dc in steps:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and heights[nr][nc] >= heights[r][c]
                    and (nr, nc) not in reachPacific):
                        todo.append((nr, nc))
                        reachPacific.add((nr, nc))

        reachAtlantic = set()
        todo = deque()
        for i in range(ROWS):
            todo.append((i, COLS - 1))
            reachAtlantic.add((i, COLS - 1))
        for i in range(COLS - 1):
            todo.append((ROWS - 1, i))
            reachAtlantic.add((ROWS - 1, i))
        
        while len(todo) > 0:
            for i in range(len(todo)):
                r, c = todo.popleft()
                steps = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for dr, dc in steps:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and heights[nr][nc] >= heights[r][c]
                    and (nr, nc) not in reachAtlantic):
                        todo.append((nr, nc))
                        reachAtlantic.add((nr, nc))

        ret = []
        for r,c in reachPacific:
            if (r, c) in reachAtlantic:
                ret.append((r,c))
        return ret


        