class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num_cols = []
        num_rows = []
        num_areas = []

        for i in range(9):
            num_cols.append(set())
            num_rows.append(set())
        for i in range(3):
            num_areas.append([])
            for j in range(3):
                num_areas[i].append(set())

        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    num = int(board[row][col])
                    if num in num_rows[row]:
                        return False
                    else:
                        num_rows[row].add(num)
                    
                    if num in num_cols[col]:
                        return False
                    else:
                        num_cols[col].add(num)

                    i1 = int((row - (row % 3)) / 3)
                    i2 = int((col - (col % 3)) / 3)
                    if num in num_areas[i1][i2]:
                        return False
                    else:
                        num_areas[i1][i2].add(num)

        return True
        