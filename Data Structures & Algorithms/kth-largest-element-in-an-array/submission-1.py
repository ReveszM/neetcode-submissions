from heapq import heappush, heappop, heapify

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = []
        for num in nums:
            if len(l) < k:
                heappush(l, num)
            elif l[0] <= num:
                heappush(l, num)
                heappop(l)
        return l[0]

        