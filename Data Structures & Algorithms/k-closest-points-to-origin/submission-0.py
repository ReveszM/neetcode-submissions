from math import sqrt
from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        for coordinates in points:
            x, y = coordinates[0], coordinates[1]
            dst = sqrt(x*x + y*y)

            if len(closest) >= k:
                curMax = closest[0][0] * (-1)
                if curMax > dst:
                    heappop(closest)
                    heappush(closest, (dst * (-1), x, y))
            else:
                heappush(closest, (dst * (-1), x, y))

        return [[x, y] for (_, x, y) in closest]
        