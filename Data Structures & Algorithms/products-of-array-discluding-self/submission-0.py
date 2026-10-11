class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProducts = [1] * len(nums)
        postfixProducts = [1] * len(nums)
        for i in range(1, len(nums)):
            prefixProducts[i] = prefixProducts[i - 1] * nums[i - 1]
        for i in range(2, len(nums) + 1):
            postfixProducts[-i] = postfixProducts[-(i - 1)] * nums[-(i - 1)]

        r = []
        for i in range(len(nums)):
            product = prefixProducts[i] * postfixProducts[i]
            r.append(product)
        return r
            

        

            



        
        