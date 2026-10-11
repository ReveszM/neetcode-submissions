class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        begin = {}
        end = {}
        maxLen = 0

        for curNum in nums:
            if curNum not in begin:
                if (curNum-1) not in begin and (curNum+1) not in begin:
                    n_begin = curNum
                    n_end = curNum
                elif (curNum-1) in begin and (curNum+1) not in begin:
                    n_begin = begin[curNum-1]
                    n_end = curNum
                elif (curNum-1) not in begin and (curNum+1) in begin:
                    n_begin = curNum
                    n_end = end[curNum+1]
                elif (curNum-1) in begin and (curNum+1) in begin:
                    n_begin = begin[curNum-1]
                    n_end = end[curNum+1]
                begin[n_begin] = n_begin
                begin[n_end] = n_begin
                end[n_begin] = n_end
                end[n_end] = n_end
                maxLen = max(maxLen, n_end-n_begin+1)

        return maxLen
        