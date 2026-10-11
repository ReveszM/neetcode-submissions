class Solution:
    def rob(self, nums: List[int]) -> int:
        money = []
        for i in range(len(nums)):
            a = nums[i] + (money[i - 2] if i >= 2 else 0)
            b = (money[i - 1] if i >= 1 else 0)
            money.append(max(a, b))
        return money[len(nums) - 1]
        

# money[i]: Maximum amount of money we can rob
# until the ith house
# money[i] = max(nums[i] + money[i - 2], money[i - 1])