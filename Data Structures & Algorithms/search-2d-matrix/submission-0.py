from math import floor

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L = 0
        R = len(matrix) - 1

        while L <= R:
            M = L + floor((R - L) / 2)

            if matrix[M][0] > target:
                R = M - 1
            elif matrix[M][0] <= target:
                L = M + 1
        row = L - 1

        L = 0
        R = len(matrix[row]) - 1

        while L <= R:
            M = L + floor((R - L) / 2)

            if matrix[row][M] > target:
                R = M - 1
            elif matrix[row][M] < target:
                L = M + 1
            else:
                return True
        return False
        

        