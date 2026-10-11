class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxs = {}
        for i in range(len(nums)):
            curNum = nums[i]
            if curNum not in idxs:
                idxs[curNum] = [i]
            else:
                idxs[curNum].append(i)

        for i in range(len(nums)):
            curNum = nums[i]
            complement = target - curNum
            if complement in idxs:
                for j in idxs[complement]:
                    if j != i:
                        return [i, j]
        
        return []

            
        