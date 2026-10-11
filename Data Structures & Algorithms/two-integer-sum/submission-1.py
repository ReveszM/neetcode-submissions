class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_index = {}

        for i in range(len(nums)):
            cur_num = nums[i]

            key = target - cur_num
            if key in nums_index:
                return [nums_index[key], i]
            else:
                nums_index[cur_num] = i
        