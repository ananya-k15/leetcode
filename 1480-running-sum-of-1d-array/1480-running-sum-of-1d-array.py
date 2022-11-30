class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l = len(nums)
        for i in range(1, l, 1) :
            nums[i] += nums[i-1]
        return nums