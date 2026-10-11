from heapq import heappush, heappop, heapify

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [(-1) * nums[i] for i in range(len(nums))]
        heapify(nums)
        for _ in range(0, k - 1):
            heappop(nums)
        return (-1) * nums[0]

        