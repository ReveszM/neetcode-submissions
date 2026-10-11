class Solution:
    def r(self, nums, index, cur_solution, solutions):
        print(f"{index}: {cur_solution}")
        if index == len(nums) - 1:
            solutions.append(cur_solution.copy())
            cur_solution.append(nums[index])
            solutions.append(cur_solution.copy())
            cur_solution.pop()
        else:
            self.r(nums, index + 1, cur_solution, solutions)
            cur_solution.append(nums[index])
            self.r(nums, index + 1, cur_solution, solutions)
            cur_solution.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        self.r(nums, 0, [], solutions)
        return solutions
        