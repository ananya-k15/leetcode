class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        n = len(nums)
        # we use backtracking
        def backtrack(current):
            nonlocal results
            # base case to add to results: length should be 3
            if len(current) == n:
                results.append(current[:])
                # return here, no other combination can be formed here
                return
            # for all values in nums
            for ind in range(0, n):
                # prune if there are duplicates
                if nums[ind] in current:
                    continue
                # add the value to current
                current.append(nums[ind])                
                # recursively call backtrack on this value
                backtrack(current)
                # remove value from current and proceed
                current.pop()
        backtrack([])
        return results