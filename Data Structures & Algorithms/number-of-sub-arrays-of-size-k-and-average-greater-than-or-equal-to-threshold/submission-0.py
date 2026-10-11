class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if k > len(arr):
            return 0
        ret = 0
        threshold = k * threshold

        L = 0
        R = k
        curSum = 0
        for i in range(k):
            curSum += arr[i]
        if curSum >= threshold:
            ret += 1

        while R < len(arr):
            curSum += arr[R]
            curSum -= arr[L]
            if curSum >= threshold:
                ret += 1
            R += 1
            L += 1

        return ret
        