from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= (-1)
        heapify(stones)

        while len(stones) > 1:
            a = heappop(stones)
            b = heappop(stones)
            remains = a - b
            if remains < 0:
                heappush(stones, remains)
        
        if len(stones) == 1:
            return (-1) * stones[0]
        else:
            return 0


        