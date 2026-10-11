class Solution:
    def climbStairs(self, n: int) -> int:
        def c(n):
            if n == 1:
                return 1
            elif n == 2:
                return 2
            else:
                return c(n-1) + c(n-2)
        return c(n)


        