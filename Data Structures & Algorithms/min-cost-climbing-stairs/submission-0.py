class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        totalCost = [0, 0, 0]
        for i in range(2, len(cost) + 1):
            totalCost[0] = totalCost[1]
            totalCost[1] = totalCost[2]

            b = totalCost[0] + cost[i - 2]
            a = totalCost[1] + cost[i - 1]
            totalCost[2] = min(a, b)
        return totalCost[2]


# totalCost[i] = min(totalCost[i-1] + cost[i-1], totalCost[i - 2] + cost[i - 2])
        