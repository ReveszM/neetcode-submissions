class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set()

        for cur_num in nums:
            if cur_num in unique_nums:
                return True
            else:
                unique_nums.add(cur_num)
        return False
        