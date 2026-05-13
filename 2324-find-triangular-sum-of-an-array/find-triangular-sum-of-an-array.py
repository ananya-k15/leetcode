class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        while len(nums) != 1:
            ind = 0
            while ind < len(nums)-1:
                nums[ind] = (nums[ind] + nums[ind+1]) % 10
                ind += 1
            nums.pop()
        
        return nums[0]