from math import floor
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        solution = max(piles)

        while L <= R:
            M = L + floor((R - L) / 2)

            curHours = 0
            for curPile in piles:
                curHours += ceil(curPile/M)
            
            if curHours <= h:
                solution = min(solution, M)
                R = M - 1
            else:
                L = M + 1

        return solution


        