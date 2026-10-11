class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        results = set()

        for m in range(0, len(nums) - 1):
            target = nums[m] * (-1)

            l, r = 0, len(nums) - 1
            while l < m and m < r:
                if nums[l] + nums[r] == target:
                    results.add(tuple([nums[l], nums[m], nums[r]]))
                    r -= 1
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1

        return list(results)        




        