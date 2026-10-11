from collections import deque

class Solution:
    def dfs(self, board: List[List[str]], a, b):
        visited = set()
        todo = deque()
        todo.append((a, b))
        visited.add((a, b))
        board[a][b] = "I"

        while len(todo) > 0:
            for i in range(len(todo)):
                cur_a, cur_b = todo.popleft()

                for da, db in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    new_a = cur_a + da
                    new_b = cur_b + db

                    if 0 <= new_a and 0 <= new_b and new_a < len(board) and new_b < len(board[0]): 
                        if board[new_a][new_b] == "O":
                            todo.append((new_a, new_b))
                            visited.add((new_a, new_b))
                            board[new_a][new_b] = "I"

                

    def solve(self, board: List[List[str]]) -> None:
        to_check = []
        to_check.extend([(0, i) for i in range(len(board[0]))])
        if len(board) > 1:
            to_check.extend([(len(board) - 1, i) for i in range(len(board[0]))])
        to_check.extend([(i, 0) for i in range(1, len(board) - 1)])
        if len(board[0]) > 1:
            to_check.extend([(i, len(board[0]) - 1) for i in range(1, len(board) - 1)])
        
        for cur_a, cur_b in to_check:
            if board[cur_a][cur_b] == "O":
                self.dfs(board, cur_a, cur_b)

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "I":
                    board[i][j] = "O"


        