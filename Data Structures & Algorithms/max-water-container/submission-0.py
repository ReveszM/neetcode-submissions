class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxWater = 0
        while l < r:
            curMaxWater = (r - l)*min(heights[l], heights[r])
            if curMaxWater > maxWater:
                maxWater = curMaxWater

            if heights[l] < heights[r]:
                l_new = l + 1
                while l_new < r and heights[l] >= heights[l_new]:
                    l_new += 1
                l = l_new
            else:
                r_new = r - 1
                while l < r_new and heights[r] >= heights[r_new]:
                    r_new -= 1
                r = r_new

        return maxWater

        