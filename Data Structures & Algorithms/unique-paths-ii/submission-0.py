class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        numRow = len(obstacleGrid)
        numCol = len(obstacleGrid[0])
        space = 0
        obstacle = 1

        prevRow = [0] * numCol
        for r in range(numRow - 1, -1, -1):
            curRow = [0] * (numCol + 1)

            for c in range(numCol - 1, -1, -1):
                if (r == numRow - 1 
                    and c == numCol - 1 
                    and obstacleGrid[-1][-1] == space):
                    curRow[c] = 1
                elif obstacleGrid[r][c] == obstacle:
                    curRow[c] = 0
                else:
                    curRow[c] = curRow[c + 1] + prevRow[c]
            prevRow = curRow
        return prevRow[0]

        