class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        
        # for each value val in nums, we want to find 
        # findTargetSumWays(target - val) and findTargetSumWays(target - val) right?
        def helper(ind, target, memo):
            key = str(target) + "," + str(ind)
            if key in memo:
                return memo[key]
            if ind < 0:
                if target == 0:
                    return 1
                else:
                    return 0
            res = 0
            if nums[ind] == 0:
                res = helper(ind-1, target, memo) * 2
            else:
                res += helper(ind-1, target - nums[ind], memo)
                res += helper(ind-1, target + nums[ind], memo)
            memo[key] = res
            return res

        return helper(len(nums)-1, target, {})

