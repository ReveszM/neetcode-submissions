class Solution:
    def rob(self, nums: List[int]) -> int:
        money = [0, 0, 0]
        for i in range(len(nums)):
            money[0] = money[1]
            money[1] = money[2]

            a = nums[i] + money[0]
            b = money[1]
            money[2] = max(a, b)
        return money[2]
        

# money[i]: Maximum amount of money we can rob
# until the ith house
# money[i] = max(nums[i] + money[i - 2], money[i - 1])