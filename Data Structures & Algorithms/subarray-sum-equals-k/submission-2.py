from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pSumIdx = defaultdict(list)
        pSumIdx[0].append(-1)
        prefSums = []
        curSum = 0
        for i in range(len(nums)):
            curSum += nums[i]
            prefSums.append(curSum)
            pSumIdx[curSum].append(i)

        r = 0
        for i in range(0, len(prefSums)):
            for curIdx in pSumIdx[prefSums[i] - k]:
                if curIdx < i:
                    r += 1
                else:
                    break
        return r
        