class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        def robMax(ind, memo={}):
            if ind == n-1: 
                return nums[ind]
            elif ind == n-2:
                return max(nums[ind], nums[ind+1])
            elif ind in memo:
                return memo[ind]
            choice1 = nums[ind] + robMax(ind+2, memo)
            choice2 = robMax(ind+1, memo)
            memo[ind] = max(choice1, choice2)
            return memo[ind]

        return robMax(0)