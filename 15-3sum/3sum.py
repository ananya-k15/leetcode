class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        results = set()

        # sort the list to get the non decreasing order of elements
        nums.sort()

        for i in range(len(nums)):
            # to get to target, we need to find j and k s.t.
            # nums[k] + nums[j] == -nums[i]
            # if nums[i] < 0, look on the right hand side
            # if nums[i] > 0, all the remaining numbers are positive 
            # so we can skip this (we would have already found a possible combo)
            if nums[i] > 0:
                break
            
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[j] + nums[k] + nums[i] == 0:
                    results.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] + nums[i] > 0:
                    k -= 1
                else:
                    j += 1
        res = [list(x) for x in results]
        return res