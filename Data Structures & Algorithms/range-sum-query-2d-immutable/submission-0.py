class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sums = []
        for i in range(len(matrix)):
            self.sums.append([])
            for j in range(len(matrix[0])):
                leftSum = self.sums[i][j - 1] if j >= 1 else 0
                aboveSum = self.sums[i - 1][j] if i >= 1 else 0
                diagonalSum = self.sums[i - 1][j - 1] if (i >= 1 and j >= 1) else 0
                curSum = leftSum + aboveSum + matrix[i][j] - diagonalSum
                self.sums[i].append(curSum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        wholeSum = self.sums[row2][col2]
        leftSum = self.sums[row2][col1 - 1] if col1 >= 1 else 0
        aboveSum = self.sums[row1 - 1][col2] if row1 >= 1 else 0
        diagonalSum = self.sums[row1 - 1][col1 - 1] if (row1 >= 1 and col1 >= 1) else 0
        return wholeSum + diagonalSum - leftSum - aboveSum
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)