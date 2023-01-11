class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = [1 for i in range(len(nums))]
        pre = 1; post = 1
        for i in range(len(nums)) : 
            prod[i] = pre
            pre *= nums[i]
        for i in range(len(nums) - 1, -1, -1) :
            prod[i] *= post
            post *= nums[i]
        return prod